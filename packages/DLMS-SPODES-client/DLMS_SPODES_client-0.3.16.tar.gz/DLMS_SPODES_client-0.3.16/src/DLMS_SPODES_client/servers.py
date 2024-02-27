import threading
from threading import Thread
from functools import cached_property
import asyncio
from queue import Queue
from typing import Any, Callable
from .client import Client, Errors, Result
from .enums import Operation
from .logger import logger
from .tasks import ExTasks


class TransactionServer:
    __t: Thread
    q_in: Queue[tuple[Operation, Client | list[Client], Any]]
    q_out: Queue

    def __init__(self):
        self.q_in = Queue()
        self.q_out = Queue()
        self.__t = Thread(
            target=self.start_coro,
            args=(self.q_in, self.q_out))
        self.__t.start()

    def start_coro(self, q_in: Queue, q_out: Queue):
        asyncio.run(self.coro_loop(q_in, q_out))

    def task(self, *args) -> threading.Event:
        a = list(args)
        a.append(ev := threading.Event())
        self.q_in.put(*args)
        return ev

    async def coro_loop(self, q_in: Queue, q_out: Queue):
        while True:
            f, dest, *a = q_in.get()
            match f, dest, *a:
                case Operation.OPEN, Client(), *_:
                    dest: Client
                    t = asyncio.create_task(dest.connect())
                    t.add_done_callback(q_out.put)
                    # await t
                case Operation.CLOSE, Client(), *_:
                    t = asyncio.create_task(dest.close())
                    t.add_done_callback(q_out.put)
                    # await t
                case Operation.INIT_TYPE, Client(), *_:
                    t = asyncio.create_task(dest.init_type())
                    t.add_done_callback(q_out.put)
                    # await t
                case Operation.READ, Client(), ln, attr:
                    t = asyncio.create_task(dest.read_attribute())
                    t.add_done_callback(q_out.put)
                    # await t
                case Operation.CLOSE, None:
                    break
                case err:
                    logger.error(F"unknown operation [{err}]", extra={"id": F"#{self.__class__.__name__}"})
            await asyncio.sleep(0.01)


class Results:
    __values: tuple[Result, ...]
    name: str

    def __init__(self, clients: tuple[Client],
                 name: str = None):
        self.__values = tuple(Result(c) for c in clients)
        self.name = name
        """common operation name"""

    def __iter__(self):
        return iter(self.__values)

    @cached_property
    def clients(self) -> set[Client]:
        return {res.client for res in self.__values}

    @cached_property
    def ok_results(self) -> set[Result]:
        """without errors exchange clients"""
        ret = set()
        for res in self.__values:
            if all(map(lambda err_code: err_code.is_ok(), res.errors)):
                ret.add(res)
        return ret

    @cached_property
    def nok_results(self) -> set[Result]:
        """ With errors exchange clients """
        return set(self.__values).difference(self.ok_results)

    def is_complete(self) -> bool:
        return all((res.complete for res in self))


class TransactionServer2:
    __t: Thread
    results: Results

    def __init__(self,
                 clients: list[Client] | tuple[Client],
                 tasks: tuple[ExTasks, ...],
                 name: str = None):
        self.results = Results(clients, name)
        self.tasks = tasks
        self._tg = None
        self.__t = Thread(
            target=self.start_coro,
            args=(self.results,))

    def start(self):
        self.__t.start()

    def start_coro(self, results):
        asyncio.run(self.coro_loop(results))

    async def coro_loop(self, results: Results):
        async with asyncio.TaskGroup() as self._tg:
            for res in results:
                self._tg.create_task(
                    coro=res.client.exchange(
                        exchanges=self.tasks,
                        result=res))
