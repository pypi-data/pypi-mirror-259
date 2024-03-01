import abc
import time
from typing import Dict, Tuple, Optional, List
import logging


class TrackerHandler(abc.ABC):
    @abc.abstractmethod
    def hparams(self, hparams: Dict):
        """Log run hparams
        Args:
            hparams: Dict -- dictionary of hparams
        """
        ...

    @abc.abstractmethod
    def log(self, metrics: Dict, step: Optional[int] = None, epoch: Optional[int] = None, context: Optional[Dict[str, str]] = None):
        ...

    @abc.abstractmethod
    def scalar(self, name, value: float, step: Optional[int] = None, epoch: Optional[int] = None, context: Optional[Dict[str, str]] = None):
        ...

    @abc.abstractmethod
    def update(self, step: Optional[int] = None, epoch: Optional[int] = None, SPU: Optional[float] = None):
        """Loop update
        """
        ...

    @abc.abstractmethod
    def close(self, completed: bool = True):
        ...


class Tracker(TrackerHandler):
    def __init__(self, handlers: List[TrackerHandler] = []) -> None:
        self.handlers = handlers
        self.num_updates = 0
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end_time = time.time()
        self.scalar("total_time_s", self.end_time - self.start_time, context={"mode": "charts"})
        self.close(exc_type is None)

    def hparams(self, hparams: Dict):
        for h in self.handlers:
            h.hparams(hparams)

    def scalar(self, name, value: float, step: int | None = None, epoch: int | None = None, context: Dict[str, str] | None = None):
        for h in self.handlers:
            h.scalar(name, value, step, epoch, context)

    def log(self, metrics: Dict, step: int | None = None, epoch: int | None = None, context: Dict[str, str] | None = None):
        for h in self.handlers:
            h.log(metrics, step, epoch, context)

    def close(self, completed : bool = True):
        for h in self.handlers:
            h.close(completed)
    
    def update(self, step: int | None = None, epoch: int | None = None, SPU: float | None = None):
        self.num_updates += 1
        SPU = (time.time() - self.start_time) / self.num_updates
        for h in self.handlers:
            h.update(step, epoch, SPU)