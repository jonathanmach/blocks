from models import Block, Folder, Page, Project
import repository

def test_tdd_domain_models():
    project = Project('Company Website')
    root_folder = project.root_folder

    page = Page('Home')
    root_folder.add_page(page)
    page.add_block(Block('Hero'))

    print(project)


def test_repository():
    project = Project('Company Website')

    project_repo = repository.ProjectRepository()
    # Alternativey, using a context manager:
    # with repository.PeeweeRepository() as project_repo:
    # https://stackoverflow.com/a/13504166/8612226
    project = project_repo.add(project)

    project = project_repo.get_by_id(project.id)

    print(project)