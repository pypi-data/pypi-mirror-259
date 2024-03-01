from __future__ import annotations

import functools
import typing as t
from dataclasses import dataclass

import result as r
import typing_extensions as te

_T = t.TypeVar("_T")
_R = t.TypeVar("_R")
_S = t.TypeVar("_S")
_P = te.ParamSpec("_P")

_TBE = t.TypeVar("_TBE", bound=BaseException)
_ReqCtxT = t.TypeVar("_ReqCtxT")
_NewCtxT = t.TypeVar("_NewCtxT")
_MigT = t.TypeVar("_MigT")
_HeadT = t.TypeVar("_HeadT")

Completer: te.TypeAlias = t.Callable[[t.Type[_T]], _T]
_Transform: te.TypeAlias = t.Callable[[_T, Completer[_ReqCtxT]], _R]


def _add_ignored_completer(f: t.Callable[[_T], _R]) -> _Transform[_T, te.Never, _R]:
    if not callable(f):
        raise TypeError

    def wrapper(__x: _T, _: Completer[t.Any]) -> _R:
        return f(__x)

    return wrapper


def flip(f: t.Callable[[_S, _T], _R]) -> t.Callable[[_T, _S], _R]:
    def wrapper(__x: _T, __y: _S) -> _R:
        return f(__y, __x)

    return wrapper


def as_result(
    *exceptions: type[_TBE],
) -> t.Callable[
    [t.Callable[_P, _R]],
    t.Callable[_P, r.Result[_R, _TBE]],
]:
    if exceptions:
        return r.as_result(*exceptions)

    def _decorator_factory(f: t.Callable[_P, _R]) -> t.Callable[_P, r.Result[_R, _TBE]]:
        def _decorator(*args: _P.args, **kwargs: _P.kwargs) -> r.Ok[_R]:
            return r.Ok(f(*args, **kwargs))

        return _decorator

    return _decorator_factory


def null_completer(typ: type) -> t.Any:
    msg = f"No completion for {typ}"
    raise RuntimeError(msg)


class LeapError(Exception):
    pass


@dataclass(frozen=True)
class Epoch(t.Generic[_HeadT, _ReqCtxT, _MigT]):
    _head: type[_HeadT]
    _inbounds: t.Sequence[
        tuple[
            _Transform[t.Any, _ReqCtxT, r.Result[_HeadT, Exception]],
            Epoch[t.Any, t.Any, t.Any],
        ],
    ]

    def __post_init__(self) -> None:
        if not isinstance(self._head, type):
            raise TypeError

        for transform, ancestor in self._inbounds:
            if not callable(transform):
                raise TypeError
            if not isinstance(ancestor, Epoch):
                raise TypeError

    def _is_supported(self, typ: type) -> bool:
        return issubclass(typ, self._head) or any(ancestor._is_supported(typ) for _, ancestor in self._inbounds)

    def ingress(
        self,
        src: type[_T],
        f: t.Callable[[_T], _HeadT],
        *fail_cond: type[Exception],
    ) -> Epoch[_HeadT, _ReqCtxT, _MigT | _T]:
        new_gen = genisis(src)
        return Epoch(
            self._head,
            [(as_result(*fail_cond)(_add_ignored_completer(f)), new_gen), *self._inbounds],  # type: ignore[arg-type]
        )

    def contextual_ingress(
        self,
        src: type[_T],
        f: _Transform[_T, _NewCtxT, _HeadT],
        *fail_cond: type[Exception],
    ) -> Epoch[_HeadT, _ReqCtxT | _NewCtxT, _MigT | _T]:
        new_gen = genisis(src)
        return Epoch(
            self._head,
            [(as_result(*fail_cond)(f), new_gen), *self._inbounds],  # type: ignore[arg-type, list-item]
        )

    def shunt(
        self,
        typ: type[_T],
        f: t.Callable[[_HeadT], _T],
        *fail_cond: type[Exception],
    ) -> Epoch[_T, _ReqCtxT, _MigT | _HeadT]:
        return Epoch(
            typ,
            [(as_result(*fail_cond)(_add_ignored_completer(f)), self)],  # type: ignore[arg-type]
        )

    def contextual_shunt(
        self,
        typ: type[_T],
        f: _Transform[_HeadT, _NewCtxT, _T],
        *fail_cond: type[Exception],
    ) -> Epoch[_T, _ReqCtxT | _NewCtxT, _MigT | _HeadT]:
        return Epoch(typ, [(as_result(*fail_cond)(f), self)])  # type: ignore[arg-type]

    def _leap_results(
        self,
        obj: _HeadT | _MigT,
        completer: Completer[_ReqCtxT],
    ) -> t.Iterator[r.Result[_HeadT, Exception]]:
        if isinstance(obj, self._head):
            yield r.Ok(obj)
            return

        yield from (
            leapt.and_then(functools.partial(flip(transform), completer))
            for transform, ancestor in self._inbounds
            for leapt in ancestor._leap_results(obj, completer)
        )

    @te.overload
    def leap(self: Epoch[_HeadT, te.Never, _MigT], obj: _HeadT | _MigT) -> _HeadT:
        ...

    @te.overload
    def leap(
        self: Epoch[_HeadT, _ReqCtxT, _MigT],
        obj: _HeadT | _MigT,
        completer: Completer[_ReqCtxT],
    ) -> _HeadT:
        ...

    def leap(self, obj: _HeadT | _MigT, completer: Completer[t.Any] = null_completer) -> _HeadT:
        if not self._is_supported(type(obj)):
            raise TypeError

        for res in self._leap_results(obj, completer):
            if isinstance(res, r.Ok):
                return res.ok_value

        msg = f"{type(self).__name__} Could not leap {obj!r}"
        raise LeapError(msg)

    def nop(self) -> te.Self:
        return self


def genisis(typ: type[_T]) -> Epoch[_T, te.Never, te.Never]:
    return Epoch(_head=typ, _inbounds=[])
