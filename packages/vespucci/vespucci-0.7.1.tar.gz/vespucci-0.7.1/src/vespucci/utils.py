import asyncio
from asyncio import Queue, create_task
from collections import Counter
from functools import wraps
from typing import (Awaitable, Callable, Generic, Hashable, List, Mapping,
                    MutableMapping, Tuple, TypeVar)

from vespucci.base import N, Tag


class _Merged(Queue):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tasks = []

    def stop(self):
        for task in self._tasks:
            task.cancel()

    def count(self, tag: Tag) -> int:  # type: ignore
        # TODO: Not too sure what the reason behind the empty body is
        pass


K = TypeVar("K", bound=Hashable)
T = TypeVar("T")


class Combined(Generic[K, T]):
    _qsize: MutableMapping[K, int]

    def __init__(self, queue: Queue):
        self._queue = queue
        self._qsize = Counter()

    async def get(self) -> Tuple[K, T]:
        (key, item) = await self._queue.get()
        self._qsize[key] -= 1
        if self._qsize[key] == 0:
            del self._qsize[key]
        return (key, item)

    async def put(self, key: K, item: T):
        self._qsize[key] += 1
        return self._queue.put((key, item))

    async def put_nowait(self, key: K, item: T):
        self._qsize[key] += 1
        return self._queue.put_nowait((key, item))

    def qsize(self, key: K) -> int:
        return self._qsize[key]


async def merge(inqs: Mapping[Hashable, Queue], **kwargs) -> Queue:
    async def move(tag, inq, outq):
        try:
            while True:
                item = await inq.get()
                await outq.put((tag, item))
        except asyncio.CancelledError:
            return

    outq = _Merged(**kwargs)

    for tag, inq in inqs.items():
        # pylint: disable=protected-access
        outq._tasks.append(create_task(move(tag, inq, outq)))

    return outq


def sequence(*funcs: Callable[[N], Awaitable[List[N]]]) -> Callable[[N], Awaitable[List[N]]]:
    async def fn(n: N) -> List[N]:
        for func in funcs:
            result = await func(n)
            if result:
                return result
        return []

    return fn


def log_exceptions(log):
    def decorator(coroutine):
        @wraps(coroutine)
        async def fn(*args, **kwargs):
            try:
                return await coroutine(*args, **kwargs)
            except Exception as exc:
                log.exception(exc)
                raise exc

        return fn

    return decorator
