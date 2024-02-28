from __future__ import annotations

from functools import partial
from typing import Any, Callable, overload


class FunctionGroup:
    def __init__(self):
        self.functions = {}

    @overload
    def register(self, func: None = None, *, name: str) -> Callable:
        ...

    @overload
    def register(self, func: Callable, *, name: None = None) -> None:
        ...

    def register(
        self, func: Callable | None = None, *, name: str | None = None
    ) -> None | Callable:
        if func is None:

            def register_func(func, name=name):
                name = name if name is not None else func.__name__
                self.functions[name] = func
                return func

            return register_func

        name = name if name is not None else func.__name__
        self.functions[name] = func
        return None

    def __call__(self, *args, **kwargs) -> Any:
        return FunctionGroupInstance(self.functions, args, kwargs)


class FunctionGroupInstance:
    def __init__(self, funcs, args, kwargs) -> None:
        self.funcs = funcs
        self.args = args
        self.kwargs = kwargs

    def __getattr__(self, name):
        if name in self.funcs:
            func = self.funcs[name]
            return partial(func, *self.args, **self.kwargs)
        raise AttributeError
