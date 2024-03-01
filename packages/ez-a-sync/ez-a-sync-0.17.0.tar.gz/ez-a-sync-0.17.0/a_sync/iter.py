
import asyncio
from a_sync._typing import *


class ASyncIterable(AsyncIterable[T], Iterable[T]):
    """An abstract iterable implementation that can be used in both a `for` loop and an `async for` loop."""
    def __iter__(self) -> Iterator[T]:
        yield from ASyncIterator.wrap(self.__aiter__())
    @classmethod
    def wrap(self, aiterable: AsyncIterable[T]) -> "ASyncWrappedIterable[T]":
        return ASyncWrappedIterable(aiterable)

class ASyncIterator(AsyncIterator[T], Iterator[T]):
    """An abstract iterator implementation that can be used in both a `for` loop and an `async for` loop."""
    def __next__(self) -> T:
        try:
            return asyncio.get_event_loop().run_until_complete(self.__anext__())
        except StopAsyncIteration as e:
            raise StopIteration from e
    @classmethod
    def wrap(self, aiterator: AsyncIterator[T]) -> "ASyncWrappedIterator[T]":
        return ASyncWrappedIterator(aiterator)

class ASyncWrappedIterable(ASyncIterable[T]):
    __slots__ = "__aiterable", 
    def __init__(self, async_iterable: AsyncIterable[T]):
        self.__aiterable = async_iterable
    def __aiter__(self) -> AsyncIterator[T]:
        return self.__aiterable.__aiter__()

class ASyncWrappedIterator(ASyncIterator[T]):
    __slots__ = "__aiterator", 
    def __init__(self, async_iterator: AsyncIterator[T]):
        self.__aiterator = async_iterator
    async def __anext__(self) -> T:
        return await self.__aiterator.__anext__()
