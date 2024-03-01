from sukta.metrics import get_default_tracker
from sukta.logging import getLogger
import time

log = getLogger("test")

with get_default_tracker(10, metrics=["loss"], logger=log) as tracker:
    tracker.hparams({
        "a": 1,
        "b": 2,
    })

    for i in range(10):
        time.sleep(0.5)
        log.info(i)
        tracker.update()