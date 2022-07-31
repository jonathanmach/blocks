from dataclasses import dataclass
from typing import List, Protocol
from models.elements import Element
import shortuuid


class Model(Protocol):
    pass


class Project:
    def __init__(self, title) -> None:
        self.id = shortuuid.uuid()
        self.title = title


@dataclass
class Schema:
    name: str
    elements: List[Element]


class Block:
    def __init__(self, name) -> None:
        self.name = name
        self.elements = []  # type: List[Element]


class Contentry:
    def __init__(self, title, slug, data, parent_id) -> None:
        self.id = shortuuid.uuid()
        self.title = title
        self.slug = slug
        self.parent_id = parent_id
        self.data = data


    def add_block(self, block: Block) -> None:
        self.blocks.append(block)


class Folder:
    def __init__(self, name, slug, parent) -> None:
        self.id = shortuuid.uuid()
        self.name = name
        self.parent = parent
        self.slug = slug
        self.folders = []  # type: List[Folder]
        self.pages = []  # type: List[Contentry]

    def add_folder(self, folder: "Folder") -> None:
        self.folders.append(folder)

    def add_page(self, page: Contentry) -> None:
        self.pages.append(page)


# class Content:  # can we think of a better name?
#     def __init__(self, name, type: Schema, folder: Folder) -> None:
#         self.name = name
#         self.type = type
#         for element in type.elements:
#             setattr(self,element.ref, None)
#         self.folder = folder
#         self.blocks = []

#     def add_block(self, block: Block) -> None:
#         self.blocks.append(block)


class Element:
    def __init__(self, name) -> None:
        self.name = name
