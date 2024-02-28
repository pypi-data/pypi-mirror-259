from typing import Any

from syrius.commands.abstract import Command
from syrius.types import InputType


class SectionSplitterCommand(Command):
    id: int = 20
    words: InputType[list[dict[str, str]]]
    text: InputType[str]