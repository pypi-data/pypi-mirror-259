from collections.abc import Iterable
from typing import Union
from uuid import UUID

from .data.classes import HotCharacter, Span


class SpanMap:
    """Hashmap to store spans and their child words for fast referencing
    and character grouping.

    Keys are span_ids and values are Span objects.
    """

    def __init__(self) -> None:
        self.span_map: dict[UUID, Span] = dict()

    def __len__(self) -> int:
        return len(self.span_map)

    def __getitem__(self, span_id: UUID) -> Union[Span, None]:
        return self.get_span(span_id)

    def __setitem__(self, span_id: UUID, hot_character: HotCharacter) -> None:
        self.insert(span_id, hot_character)

    def items(self) -> Iterable[tuple[UUID, Span]]:
        yield from self.span_map.items()

    def insert(self, span_id: UUID, hot_character: HotCharacter) -> None:
        span = self.span_map.get(span_id)
        if not span:
            span = Span(
                characters=[],
                span_id=span_id,
            )
        span.characters.append(hot_character)
        self.span_map[span_id] = span

    def get_span(self, span_id: UUID) -> Union[Span, None]:
        span = self.span_map.get(span_id)
        if not span:
            return None
        span.characters = sorted(span.characters, key=lambda ch: (ch.y, ch.x))
        return span
