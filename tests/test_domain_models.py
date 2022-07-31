from models import Block, Schema, Contentry, Project

# from models.base import Content
import repository
from models.elements import ContainerElement, StringElement


def test_tdd_domain_models():
    project = Project("Company Website")
    root_folder = project.root_folder

    page = Contentry("Home", root_folder)
    root_folder.add_page(page)
    page.add_block(Block("Hero"))

    # Schema and elements
    page_schema = Schema(
        "Page",
        [StringElement("Title", "title"), ContainerElement("Content", "content")]
    )
    # page = Content('Home', page_schema, root_folder)
    # I would expect this Page content to have a title property and a container property
    print(0)


def test_repository():
    project_repo = repository.ProjectRepository()
    project = Project("Company Website")

    project = project_repo.add(project)
    project = project_repo.get_by_id(project.id)

    # Page
    entry = Contentry("Home", None, project.root_folder)
    contentry_repo = repository.ContentryRepository()
    entry = contentry_repo.add(entry)


    entry = contentry_repo.get(entry.slug)

    print(0)
