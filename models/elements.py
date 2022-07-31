from abc import ABC
from typing import Protocol
from unicodedata import name


class Element (ABC):
    type: str

    def __init__(self, name, ref):
        self.name = name
        self.ref = ref


class StringElement(Element):
    type = 'string'

class ImageElement(Element):
    type = 'image'

class RichTextElement(Element):
    type = 'rich_text'


class ContainerElement(Element):
    type = 'container'

