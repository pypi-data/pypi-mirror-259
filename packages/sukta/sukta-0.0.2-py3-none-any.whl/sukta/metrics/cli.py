from typing import Dict, Tuple
import time
import sukta.tree_util as stu
import logging
from sukta.metrics.tracker import TrackerHandler

from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.panel import Panel
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn


class CLITrackerHandler(TrackerHandler):
    def __init__(
        self, 
        total_updates: int | None = None, 
        logger: logging.Logger | None = None,
        metrics: Tuple[str] = ()
    ):
        self.total_updates = total_updates
        self.logger = logger
        self.metrics = metrics
        self.console = None
        if self.logger is not None:
            for handler in self.logger.handlers:
                if isinstance(handler, RichHandler):
                    self.console = handler.console
        self.console = self.console or Console()

        if total_updates is not None:
            self.job_progress = Progress(SpinnerColumn(), *Progress.get_default_columns(), TimeElapsedColumn())
            self.job_task = self.job_progress.add_task("[green]Updates", total=self.total_updates - 1)
            self.live = Live(self._generate_status_table(), console=self.console).__enter__()

    def hparams(self, hparams: Dict):
        table = Table(title="HParams")
        table.add_column("key", justify="left", style="cyan")
        table.add_column("value", justify="right", style="green")
        for k, v in stu.iter_path(hparams):
            table.add_row(k, str(v))
        if self.logger is None:
            self.console.print(table)
        else:
            console = Console()
            with console.capture() as capture:
                console.print(table)
            table = Text.from_ansi(capture.get())
            self.logger.info(table, extra={"markup": True})

    def log(self, metrics: Dict, step: int | None, epoch: int | None, context: Dict[str, str] | None = None):
        return super().log(metrics, step, epoch, context)

    def scalar(self, name, value: float, step: int | None, epoch: int | None, context: Dict[str, str] | None = None):
        if self.logger:
            self.logger.info("{0}: {1} [step={2}, epoch={3}] {4}".format(name, value, step, epoch, context))
        else:
            self.console.log("{0}: {1} [step={2}, epoch={3}] {4}".format(name, value, step, epoch, context))

    def update(self, step: int | None = None, epoch: int | None = None, SPU: float | None = None):
        self.job_progress.advance(self.job_task)
        self.live.update(self._generate_status_table())

    def close(self, completed = True):
        self.live.__exit__(None, None, None)
    
    def generate_metric_table(self):
        self.metric_table = Table(title="Metric Summary")
        self.metric_table.add_column("metric", justify="left")
        self.metric_table.add_column("value", justify="right")
        for k in self.metrics:
            self.metric_table.add_row(k, str(time.time()))
        return self.metric_table

    def _generate_status_table(self):
        progress_table = Table.grid()
        if len(self.metrics):
            progress_table.add_row(self.generate_metric_table())
        progress_table.add_row(Panel.fit(
            self.job_progress, title="[b]Progress", border_style="green",
        ))
        return progress_table