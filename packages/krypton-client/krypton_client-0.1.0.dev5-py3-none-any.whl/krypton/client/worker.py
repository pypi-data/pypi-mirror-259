import threading
from typing import Callable, TypeAlias

from kryptostav.lib.model.struct import DataFrameSharedResource

Period: TypeAlias = float
SDFMap: TypeAlias = dict[str, SharedDataFrame]
StepCB: TypeAlias = Callable[['Worker'], None]

class Worker:
    DEFAULT_PERIOD: Period = 1.0

    def __init__(
            self,
            period: Period|None = None,
            stepcb: StepCB|None = None,
            sdfmap: SDFMap|None = None,
    ):
        self.__period = period or self.DEFAULT_PERIOD
        self.__stepcb = stepcb or (lambda _: _)
        self.__sdfmap = sdfmap or {}
        self.__event_stop = threading.Event()
        self.__event_wait = threading.Event()
        self.__thread = None

    def __getitem__(self, key: str) -> SharedDataFrame:
        return self.__sdfmap[key]

    def start(self):
        if self.__thread is None:
            self.__event_stop.clear()
            self.__event_wait.clear()
            self.__thread = threading.Thread(target=self.run)
            self.__thread.start()

    def end(self):
        if self.__thread is not None and self.__thread.is_alive():
            self.__event_stop.set()
            self.__event_wait.set()
            self.__thread.join()

    def run(self):
        while not self.__event_stop.is_set():
            self.__stepcb(self)
            self.__event_wait.wait(timeout=self.__period)
            self.__event_wait.clear()
