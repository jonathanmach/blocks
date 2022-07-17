from abc import ABC, abstractmethod
from orm import peewee_orm
from models import Folder, Project


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError


class PeeweeBaseRepository(AbstractRepository):
    model = None

    def add(self, model):
        return self.model.create(name=model.name).to_domain_model()

    def get_by_id(self, id: str):
        return self.model.get_by_id(id).to_domain_model()


class ProjectRepository(PeeweeBaseRepository):
    model = peewee_orm.Project

    def add(self, project: Project):
        root_folder = peewee_orm.Folder.create(name='Root')
        project = peewee_orm.Project.create(name=project.name, root_folder=root_folder) # type: peewee_orm.Project
        return project.to_domain_model()

