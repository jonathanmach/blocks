from typing import List


class Project:
    def __init__(self, name) -> None:
        self.name = name
        self._root_folder = Folder('Root')

class Block:
    def __init__(self, name) -> None:
        self.name = name
        self.elements = [] # type: List[Element]

class Page:
    def __init__(self, name) -> None:
        self.name = name
        self.blocks = []

    def add_block(self, block: Block) -> None:
        self.blocks.append(block)

class Folder:
    def __init__(self, name) -> None:
        self.name = name
        self.folders = [] # type: List[Folder]
        self.pages = [] # type: List[Page]

    def add_folder(self, folder: 'Folder') -> None:
        self.folders.append(folder)

    def add_page(self, page: Page) -> None:
        self.pages.append(page)


class Element:
    def __init__(self, name) -> None:
        self.name = name
