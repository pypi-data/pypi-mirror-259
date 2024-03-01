from __future__ import annotations

import json
import typing as t
from dataclasses import dataclass

import pytest
import typing_extensions as te

import titi


@dataclass
class Str:
    x: str

    def to_int(self) -> Int:
        return Int(y=int(self.x))

    @classmethod
    def from_json(cls, json_str: str) -> Str:
        return cls(**json.loads(json_str))


@dataclass
class Int:
    y: int

    def to_float(self) -> Float:
        return Float(z=float(self.y))

    @classmethod
    def from_json(cls, json_str: str) -> Int:
        return cls(**json.loads(json_str))


@dataclass
class Float:
    z: float

    @classmethod
    def from_json(cls, json_str: str) -> Float:
        return cls(**json.loads(json_str))

    @classmethod
    def from_float(cls, number: float) -> Float:
        return Float(z=number)

    def to_float2(self, extra: titi.Completer[float]) -> Float2:
        return Float2(self, b=extra(float))


@dataclass
class Float2:
    a: Float
    b: float


_SG: te.TypeAlias = titi.Epoch[Float, te.Never, str | Str | Int | float]
_NC: te.TypeAlias = titi.Epoch[Float2, float, str | Str | Int | Float | float]


@pytest.fixture
def simple_graph() -> _SG:
    graph = (
        titi.genisis(Str)
        .ingress(str, Str.from_json, TypeError, json.JSONDecodeError)
        .nop()
        .shunt(Int, Str.to_int)
        .ingress(str, Int.from_json, TypeError, json.JSONDecodeError)
        .nop()
        .shunt(Float, Int.to_float)
        .ingress(float, Float.from_float)
        .ingress(str, Float.from_json, TypeError, json.JSONDecodeError)
    )
    return graph


@pytest.mark.parametrize(
    "inp",
    ['{"x": "10"}', '{"y": 10}', '{"z": 10.0}', Str(x="10"), Int(y=10), 10.0],
    ids=repr,
)
def test_leap_properly_leaps_all_leaves(simple_graph: _SG, inp: t.Any) -> None:
    assert simple_graph.leap(inp) == Float(z=10.0)


def test_api_missuse_raises_type_errors(simple_graph: _SG) -> None:
    with pytest.raises(TypeError):
        # first pos should be an instance of "type"
        simple_graph.shunt(1, lambda x: x)  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        # second pos should be a callable
        simple_graph.shunt(int, 1)  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        # first pos should be an instance of "type"
        simple_graph.ingress(1, lambda x: x)  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        # second pos should be a callable
        simple_graph.ingress(int, 1)  # type: ignore[arg-type]


@pytest.mark.parametrize("inp", ['{"a": 10}', "invalid_json"], ids=repr)
def test_leap_fails_on_not_applicable_input(simple_graph: _SG, inp: str) -> None:
    with pytest.raises(titi.LeapError):
        simple_graph.leap(inp)


def test_leap_raises_type_error_if_input_is_of_wrong_type(simple_graph: _SG) -> None:
    with pytest.raises(TypeError):
        simple_graph.leap(None)  # type: ignore[call-overload]


@pytest.mark.parametrize("inp", ['{"a": 10}', "invalid_json"], ids=repr)
def test_leap_exhausted_error_message_contain_input(simple_graph: _SG, inp: str) -> None:
    with pytest.raises(titi.LeapError, match=inp):
        simple_graph.leap(inp)


@pytest.fixture
def needs_extra_context(simple_graph: _SG) -> _NC:
    nc = simple_graph.contextual_shunt(Float2, Float.to_float2)
    return nc


def test_raises_error_if_no_completer_is_provided(needs_extra_context: _NC) -> None:
    with pytest.raises(RuntimeError, match=f"No completion for {float!s}"):
        needs_extra_context.leap('{"x": 10}')  # type: ignore[call-arg]


def test_can_leap_if_completer_is_provided(needs_extra_context: _NC) -> None:
    def completer(t: type[float]) -> float:
        assert issubclass(t, float)
        return 42.0

    leapd = needs_extra_context.leap('{"x": "10"}', completer)
    assert leapd == Float2(a=Float(10.0), b=42.0)


@pytest.mark.parametrize("exception_type", [ValueError, TypeError, RuntimeError])
def test_leap_fails_with_completer_error_if_completer_raises(
    needs_extra_context: _NC, exception_type: type[Exception]
) -> None:
    def completer(_: t.Any) -> float:
        msg = "In completer!"
        raise exception_type(msg)

    with pytest.raises(exception_type, match="In completer!"):
        _ = needs_extra_context.leap('{"x": "10"}', completer)
