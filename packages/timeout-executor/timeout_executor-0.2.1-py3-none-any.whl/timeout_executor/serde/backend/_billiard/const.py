from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from timeout_executor.serde.main import PicklerType


unpatch: frozenset[PicklerType] = frozenset({"pickle"})
replace: dict[PicklerType, PicklerType] = {"pickle": "dill"}
order: tuple[PicklerType, ...] = ("dill", "cloudpickle")
