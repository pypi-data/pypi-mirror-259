from __future__ import annotations

import pathlib


def test_readme_pipe():
    from operator import itemgetter

    from functools_extra import pipe

    def add_one(x: int) -> int:
        return x + 1

    assert pipe(range(3), list, itemgetter(2), add_one) == 3  # noqa: PLR2004


def test_readme_pipe_builder():
    from functools_extra import pipe_builder

    def add_one(x: int) -> int:
        return x + 1

    def double(x: int) -> int:
        return x * 2

    add_one_and_double = pipe_builder(add_one, double)
    assert add_one_and_double(1) == 4  # noqa: PLR2004
    assert add_one_and_double(2) == 6  # noqa: PLR2004


def test_readme_functiongroup(tmp_path: pathlib.Path):
    import json
    from typing import Protocol

    from functools_extra import FunctionGroup

    class DictIO(Protocol):
        def save_dict(self, dict_: dict[str, str]) -> None:
            ...

        def load_dict(self) -> dict[str, str]:
            ...

    class JsonDictIO(DictIO):
        def __init__(self, file_name: str):
            self.file_name = file_name

        def save_dict(self, dict_: dict[str, str]) -> None:
            with open(self.file_name, "w") as f:
                json.dump(dict_, f)

        def load_dict(self) -> dict[str, str]:
            with open(self.file_name) as f:
                return json.load(f)

    json_dict_io = FunctionGroup()

    @json_dict_io.register(name="save_dict")
    def save_dict(dict_: dict[str, str], file_name: str) -> None:
        with open(file_name, "w") as f:
            json.dump(dict_, f)

    @json_dict_io.register
    def load_dict(file_name: str) -> dict[str, str]:
        with open(file_name) as f:
            return json.load(f)

    d = {"function": "group"}

    # test conventional implementation
    file_name = str(tmp_path / "test_conv.json")
    json_io = JsonDictIO(file_name)
    json_io.save_dict(d)
    assert json_io.load_dict() == d
    with open(file_name) as f:
        assert f.read() == '{"function": "group"}'

    # test FunctionGroup implementation
    file_name = str(tmp_path / "test_functiongroup.json")
    json_io = json_dict_io(file_name=file_name)
    json_io.save_dict(d)
    assert json_io.load_dict() == d
    with open(file_name) as f:
        assert f.read() == '{"function": "group"}'
