from __future__ import annotations

from threading import get_native_id
from time import sleep
from typing import Any, cast

from click import command, option
from loguru import logger
from luigi import IntParameter, Task
from numpy import arange, array
from numpy.random import default_rng
from typing_extensions import override

from utilities.atomicwrites import writer
from utilities.logging import LogLevel
from utilities.loguru import setup_loguru
from utilities.luigi import PathTarget, build
from utilities.os import CPU_COUNT
from utilities.pathvalidate import valid_path
from utilities.random import SYSTEM_RANDOM
from utilities.tempfile import TEMP_DIR
from utilities.types import get_class_name


class Example(Task):
    """Example task."""

    messages = cast(int, IntParameter())

    @override
    def output(self) -> PathTarget:  # type: ignore
        return PathTarget(valid_path(TEMP_DIR, get_class_name(self)))

    @override
    def run(self) -> None:
        rng = default_rng(get_native_id())
        levels = [level.name for level in LogLevel]
        p = array([40, 30, 20, 9, 1]) / 100.0
        for i in arange(n := self.messages) + 1:
            level = rng.choice(levels, p=p)
            logger.log(level, "{}, #{}/{}", get_class_name(self), i, n)
            sleep(1.0 + SYSTEM_RANDOM.random())
        with writer(self.output().path) as temp:
            temp.touch()


@command()
@option("-t", "--tasks", default=10)
@option("-m", "--messages", default=60)
def main(*, tasks: int, messages: int) -> None:
    """Run the test script."""
    setup_loguru(levels={"luigi": LogLevel.DEBUG}, files="test_luigi")
    classes = [type(f"Example{i}", (Example,), {}) for i in range(tasks)]
    instances = [cast(Example, cast(Any, cls)(messages=messages)) for cls in classes]
    _ = build(instances, local_scheduler=True, workers=CPU_COUNT)


if __name__ == "__main__":
    main()
