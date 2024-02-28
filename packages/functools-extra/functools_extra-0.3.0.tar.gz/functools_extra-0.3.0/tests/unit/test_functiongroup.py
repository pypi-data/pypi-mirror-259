from __future__ import annotations

from typing import Protocol, runtime_checkable

from functools_extra import FunctionGroup


@runtime_checkable
class MyProtocol(Protocol):
    def func_1(self, arg: int, arg_2: str) -> tuple[int, str]:
        ...

    def func_2(self, arg: int) -> int:
        ...


func_group = FunctionGroup()


@func_group.register(name="func_1")
def func_xxx(arg: int, arg_2: str, common: str):
    return arg, arg_2, common


@func_group.register
def func_2(arg: int, common: str):
    return arg, common


def test_function_group():
    proto = func_group(common="int")
    assert proto.func_1(1, "1") == (1, "1", "int")
    assert proto.func_2(2) == (2, "int")
    assert isinstance(proto, MyProtocol)
    # check if accessing other attributes still works
    proto.test = "test"  # type: ignore [attr-defined]
    assert proto.test == "test"  # type: ignore [attr-defined]
