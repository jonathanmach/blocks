from main import Block, Folder, Page, Project


def test_tdd_domain_models():
    project = Project('Company Website')
    root_folder = project._root_folder

    page = Page('Home')
    root_folder.add_page(page)
    page.add_block(Block('Hero'))

    print(project)

