import math
from collections import defaultdict
from collections.abc import Generator
from typing import Union
from uuid import UUID, uuid4

from pdfminer.layout import LTAnno, LTChar, LTComponent, LTFigure, LTPage, LTText, LTTextContainer, LTTextLine

from .data.classes import HotCharacter, PageResult
from .span_map import SpanMap
from .sparse_matrix import SparseMatrix
from .trie import Trie


class MemoryMap:
    def __init__(self) -> None:
        """Initialize the MemoryMap. 2D Matrix representation of a PDF Page.

        Args:
            width (int): The width (max columns) of a page.
            height (int) The height (max rows) of a page.
        """
        self.text_trie = Trie()
        self.span_map = SpanMap()
        self.width: int = 0
        self.height: int = 0

    def build_memory_map(self) -> None:
        """Build the memory map based on width and height.

        The memory map is a SparseMatrix representation of the PDF.
        """
        self.memory_map = SparseMatrix()

    def __reverse_page_objs(self, page_objs: list[LTComponent]) -> Generator[LTComponent, None, None]:
        yield from reversed(page_objs)

    def __extract_from_ltfigure(self, lt_figure_obj: LTFigure) -> Generator[Union[LTTextLine, LTChar], None, None]:
        for element in lt_figure_obj:
            if isinstance(element, (LTTextLine, LTChar)):
                yield element
            elif isinstance(element, LTTextContainer):
                element_stack = self.__reverse_page_objs(list(element))
                yield from (em for em in element_stack if isinstance(em, LTTextLine))

    def __get_page_spans(self, page: LTPage) -> Generator[Union[LTTextLine, LTChar], None, None]:
        element_stack = self.__reverse_page_objs(page._objs)
        for obj in element_stack:
            if isinstance(obj, LTTextLine):
                yield obj
            elif isinstance(obj, (LTTextContainer)):
                element_stack = self.__reverse_page_objs(list(obj))
                yield from (em for em in element_stack if isinstance(em, LTTextLine))
            elif isinstance(obj, (LTFigure)):
                yield from self.__extract_from_ltfigure(obj)

    def __get_right_shifted_hot_character(self, hot_character: HotCharacter, shift: int) -> HotCharacter:
        """Shift a hotcharacter on the x-coordinate

        Args:
            hot_character (HotCharacter): HotCharacter object to be shifted
            shift (int): shift offset on the x-coordinate

        Returns:
            HotCharacter: HotCharacter object with new coords
        """
        hot_character.x += shift
        hot_character.x_end += shift
        return hot_character

    def load_memory_map(
        self,
        page: LTPage,
        include_annotation_spaces: bool = False,
        preserve_pdfminer_coordinates: bool = False,
    ) -> None:
        """Load memory map data from an XML page.

        Args:
            page (str): LTPage Element returned by pdfminer
            include_annotation_spaces (bool, optional): Add annotation spaces to the memory map.
            preserve_pdfminer_coordinates(bool, optional): Preserve pdfminer y-coordinate values.
        Returns:
            None
        """
        char_hot_characters: list[HotCharacter] = []
        page_components: Generator[Union[LTTextLine, LTChar], None, None] = self.__get_page_spans(page)
        line_shift: defaultdict[int, int] = defaultdict(int)
        for component in page_components:
            span_id = uuid4()
            prev_char_inserted = False
            if isinstance(component, LTChar):
                x0 = round(component.x0)
                x1 = round(component.x1)
                y0 = round(component.y0) if preserve_pdfminer_coordinates else round(page.height - component.y0)
                hot_character: HotCharacter = self.__get_hot_character_of(
                    value=component.get_text(),
                    x=x0,
                    y=y0,
                    x_end=x1,
                    span_id=span_id,
                )
                char_hot_characters.append(
                    hot_character,
                )
                continue
            for character in component:
                if (
                    include_annotation_spaces
                    and isinstance(character, LTAnno)
                    and (character._text == " ")
                    and prev_char_inserted
                ):
                    _elem_width: int = 1
                    space_char: HotCharacter = self.__get_hot_character_of(
                        value=" ", x=x0, y=y0, x_end=x0 + _elem_width, span_id=span_id, is_anno=True
                    )
                    char_hot_characters.append(
                        space_char,
                    )
                    prev_char_inserted = False
                elif (
                    isinstance(character, (LTChar, LTText))
                    and (
                        hasattr(character, "x0")
                        and hasattr(character, "x1")
                        and hasattr(character, "y0")
                        and hasattr(character, "y1")
                    )
                    and not isinstance(character, LTAnno)
                ):
                    char_c = character.get_text()
                    x0 = round(character.x0)
                    x1 = round(character.x1)
                    y0 = round(component.y0) if preserve_pdfminer_coordinates else round(page.height - component.y0)
                    hot_character = self.__get_hot_character_of(
                        value=char_c,
                        x=x0,
                        y=y0,
                        x_end=x1,
                        span_id=span_id,
                    )
                    char_hot_characters.append(
                        hot_character,
                    )
                    prev_char_inserted = char_c != " "
        # Insert into Trie and Span Maps
        last_inserted_x_y: tuple[int, int] = (-1, -1)
        for i in range(len(char_hot_characters)):
            _current_character: HotCharacter = char_hot_characters[i]
            # Determine if annotation spaces should be added
            if include_annotation_spaces and i > 0 and i < len(char_hot_characters) - 1:
                prev_char: HotCharacter = char_hot_characters[i - 1]
                next_char: HotCharacter = char_hot_characters[i + 1]
                # Anno and non-anno characters should not be overlapping
                if _current_character.is_anno and next_char.x - prev_char.x <= 0:
                    continue

            # Prevent characters from overlapping
            if (last_inserted_x_y[0] > 0 and last_inserted_x_y[1] > 0) and (
                _current_character.x == last_inserted_x_y[0] and _current_character.y == last_inserted_x_y[1]
            ):
                line_shift[_current_character.y] += 1
            last_inserted_x_y = (_current_character.x, _current_character.y)
            _current_character = self.__get_right_shifted_hot_character(
                _current_character, line_shift[_current_character.y]
            )

            self.__insert_hotcharacter_to_memory(_current_character)
        self.width = math.ceil(page.width)
        self.height = math.ceil(page.height)

    def __insert_hotcharacter_to_memory(
        self,
        hot_character: HotCharacter,
    ) -> None:
        """Insert hotcharacter into memory map & trie"""
        if hot_character.value == "":
            return None
        self.memory_map.insert(value=hot_character.value, row_idx=hot_character.y, column_idx=hot_character.x)
        self.text_trie.insert(word=hot_character.value, hot_character=hot_character)
        if hot_character.span_id:
            self.span_map[hot_character.span_id] = hot_character

    def __get_hot_character_of(
        self,
        value: str,
        x: int,
        y: int,
        x_end: int,
        span_id: UUID,
        is_anno: bool = False,
    ) -> HotCharacter:
        """Insert element into memory map.

        Args:
            value (str): Value of the object to be inserted.
            x (int): column index (x0-coordinate) of the element.
            y (int): row index (y0-coordinate) of the element.
            x_end (int): end column index (x1-coordinate) of element. x_end - x = width of element.
            span_id (UUID): id of parent span.

        Returns:
            HotCharacter: HotCharacter object of the whitespace.
        """
        return HotCharacter(
            value=value,
            x=x,
            y=y,
            x_end=x_end,
            span_id=span_id,
            is_anno=is_anno,
        )

    def extract_text_from_bbox(self, x0: int, x1: int, y0: int, y1: int) -> str:
        """Extract text within a specified bounding box.

        Args:
            x0 (int): Left x-coordinate of the bounding box.
            x1 (int): Right x-coordinate of the bounding box.
            y0 (int): Bottom y-coordinate of the bounding box.
            y1 (int): Top y-coordinate of the bounding box.

        Returns:
            str: Extracted text within the bounding box.
        """
        extracted_text: str = ""
        for row in range(max(y0, 0), min(y1, self.memory_map.rows - 1) + 1):
            row_text: str = ""
            row_text = "".join(
                self.memory_map.get(row_idx=row, column_idx=col)
                for col in range(max(x0, 0), min(x1, self.memory_map.columns - 1) + 1)
            )
            if row_text:
                extracted_text += row_text + "\n"

        return extracted_text

    def find_text(self, query: str) -> tuple[list[str], PageResult]:
        """Find text within the memory map.

        Args:
            query (str): The text to search for.

        Returns:
            list: List of found text coordinates.
        """
        found_text = self.text_trie.search_all(query)
        return found_text
