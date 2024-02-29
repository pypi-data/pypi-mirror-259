from __future__ import annotations

from functools import wraps
from typing import Any, AsyncContextManager, Callable, Coroutine, Generator, TypeVar

from .cursor import Cursor

_T = TypeVar("_T")

class Result(AsyncContextManager[_T], Coroutine[Any, Any, _T]):
    def __init__(self, coro: Coroutine[Any, Any, _T]) -> None:
        self._coro = coro
        self._obj: _T

    def send(self, value):
        return self._coro.send(value)

    def throw(self, type, value=None, traceback=None):
        if value is None:
            return self._coro.throw(type, value)

        if traceback is None:
            return self._coro.throw(type, value)

        return self._coro.throw(type, value, traceback)

    def close(self):
        return self._coro.close()

    def __await__(self):
        return self._coro.__await__()

    async def __aenter__(self) -> _T:
        self._obj = await self._coro
        return self._obj

    async def __aexit__(self, exc_type, exc, tb):
        if isinstance(self._obj, Cursor):
            await self._obj.close()

def contextmanager(
    method: Callable[..., Coroutine[Any, Any, _T]]
) -> Callable[..., Result[_T]]:
    @wraps(method)
    def wrapper(*args, **kwargs) -> Result[_T]:
        return Result(method(*args, **kwargs))
    return wrapper