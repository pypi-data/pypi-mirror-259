import asyncio
from uuid import uuid4
import logging
from contextlib import AsyncExitStack
from typing import Generic, Set, TypeVar, Optional

from vespucci.oracle import Oracle
from vespucci.store import Store
from vespucci.base import Tag
from vespucci.utils import log_exceptions

log = logging.getLogger(__name__)


N = TypeVar("N")


class Crawler(Generic[N]):
    _visited: Set[N]
    _LOG_FREQUENCY = 100

    def __init__(
        self, oracle: Oracle[N], store: Store[N], tag: Optional[Tag] = None, capacity: int = 10
    ):
        self._oracle = oracle
        self._store = store
        self._tag = tag or str(uuid4())
        self._capacity = capacity
        self._process_task = None
        self._visited = set()
        self._n_edges = 0

    async def seed(self, node: N, rank: int):
        await self._oracle.seed(self._tag, node, rank)
        self._visited.add(node)

    @log_exceptions(log)
    async def _process(self):
        self._n_edges = 0
        async for (edge, rank) in self._oracle.reveal(self._tag):
            log.debug("Crawler %s found edge %s of rank %d", self._tag, edge, rank)
            await self._store.save(edge)
            if edge.dst is not None:
                self._n_edges += 1
                if self._n_edges % self._LOG_FREQUENCY == 0:
                    log.info("Crawler %s traversed %d edges", self._tag, self._n_edges)

            if rank > 1 and edge.dst is not None and edge.dst not in self._visited:
                await self.seed(edge.dst, rank - 1)
            else:
                in_process = self._oracle.in_process(self._tag)
                log.debug("Crawler %s has %d nodes in process", self._tag, in_process)
                if in_process <= 0:
                    log.info("Crawler %s traversed %d edges", self._tag, self._n_edges)
                    return

    def run(self):
        return self._process_task

    def status(self):
        return {
            "active_nodes": self._oracle.in_process(self._tag),
            "traversed_edges": self._n_edges,
        }

    async def __aenter__(self):
        self._oracle.register(self._tag, self._capacity)
        self._process_task = asyncio.create_task(self._process())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self._process_task.done():
            self._process_task.cancel()
        self._oracle.unregister(self._tag)

    async def enter(self, stack: AsyncExitStack):
        return await stack.enter_async_context(self)
