from typing import Tuple
import logging

from .tracker import Tracker
from .cli import CLITrackerHandler
from .aim import AimTrackerHandler

def get_default_tracker(
    total_updates: int | None = None,
    run_hash: str | None = None,
    experiment: str | None = None, 
    logger: logging.Logger | None = None,
    metrics: Tuple[str] = (),
):
    return Tracker(
        handlers=[
            CLITrackerHandler(total_updates, logger, metrics),
            AimTrackerHandler(run_hash, experiment, metrics),
        ]
    )