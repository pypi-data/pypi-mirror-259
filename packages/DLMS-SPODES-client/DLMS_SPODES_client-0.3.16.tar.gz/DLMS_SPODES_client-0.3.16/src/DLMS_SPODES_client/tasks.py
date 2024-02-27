from dataclasses import dataclass
from abc import ABC
from typing import TypeAlias


class ExTask(ABC):
    """Exchange task for DLMS client"""


class InitType(ExTask):
    """nothing params"""


@dataclass
class ReadAttribute(ExTask):
    ln: str
    index: int


@dataclass
class WriteAttribute(ExTask):
    ln: str
    index: int
    value: bytes | str


ExTasks: TypeAlias = InitType | ReadAttribute | WriteAttribute
