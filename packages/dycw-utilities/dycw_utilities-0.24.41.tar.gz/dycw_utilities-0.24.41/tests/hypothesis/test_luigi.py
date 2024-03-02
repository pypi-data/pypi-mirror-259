from __future__ import annotations

from typing import Any

from hypothesis import given
from hypothesis.strategies import DataObject, data
from luigi import Task

from utilities.hypothesis import namespace_mixins


class TestNamespaceMixins:
    @given(data=data())
    def test_main(self, *, data: DataObject) -> None:
        _ = data.draw(namespace_mixins())

    @given(namespace_mixin=namespace_mixins())
    def test_first(self, *, namespace_mixin: Any) -> None:
        class Example(namespace_mixin, Task):
            ...

        _ = Example()

    @given(namespace_mixin=namespace_mixins())
    def test_second(self, *, namespace_mixin: Any) -> None:
        class Example(namespace_mixin, Task):
            ...

        _ = Example()
