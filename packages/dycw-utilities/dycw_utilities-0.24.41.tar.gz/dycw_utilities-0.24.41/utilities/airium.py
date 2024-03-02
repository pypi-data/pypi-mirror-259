from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any, cast

from airium import Airium


@contextmanager
def yield_airium() -> Iterator[Airium]:
    """Yield an `Airium` object with the docstyle set to HTML."""
    airium = Airium()
    airium("<!DOCTYPE html>")
    with cast(Any, airium).html().body():
        yield airium


__all__ = ["yield_airium"]
