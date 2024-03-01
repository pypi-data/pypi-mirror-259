import sukta.tree_util as stu
from typing import Dict, Tuple 
from sukta.metrics.tracker import TrackerHandler
from aim import Run


class AimTrackerHandler(TrackerHandler):
    def __init__(self, run_hash: str | None = None, experiment: str | None = None, metrics: Tuple[str] = ()):
        self.run = Run(
            run_hash=run_hash,
            experiment=experiment,
            log_system_params=True,
            capture_terminal_logs=True
        )
        self.metrics = metrics

    def hparams(self, hparams: Dict):
        self.run['hparams'] = hparams

    def log(self, metrics: Dict, step: int | None, epoch: int | None, context: Dict[str, str] | None = None):
        for k, v in stu.iter_path(metrics):
            self.scalar(k, v, step, epoch, context)

    def scalar(self, name, value: float, step: int | None, epoch: int | None, context: Dict[str, str] | None = None):
        self.run.track(value, name=name, step=step, epoch=epoch, context=context)

    def update(self, step: int | None, epoch: int | None, SPU: float | None):
        self.run.report_progress(expect_next_in=SPU * 2)

    def close(self, completed: bool = True):
        self.run.report_successful_finish()
