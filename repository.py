from abc import ABC, abstractmethod
from orm import peewee_orm
from models import Model, Contentry, Project


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError


# In-memory repository
in_memory_db = {}
class InMemoryProjectRepository(AbstractRepository):
    def __init__(self) -> None:
        in_memory_db["projects"] = {}
        self.db = in_memory_db["projects"]

    def add(self, model: Model):
        self.db[model.id] = model
        return model

    def get_by_id(self, id):
        project = self.db.get(id)
        if project is None:
            raise Exception("Project not found")
        return project

class InMemoryContentRepository(AbstractRepository):
    def __init__(self) -> None:
        in_memory_db["content"] = {}
        self.db = in_memory_db["content"]

    def add(self, model: Model):
        self.db[model.id] = model
        return model

    def get_by_id(self, id):
        project = self.db.get(id)
        if project is None:
            raise Exception("Content not found")
        return project

    def get_by_slug(self, slug):
        iterator =  filter(lambda contentry: contentry.slug == slug , self.db.values())
        try:
            content = next(iterator)
            return content
        except StopIteration:
            raise Exception("Content not found")
        

    def get_by_folder(self, folder_id):
        iterator =  filter(lambda contentry: contentry.parent_id == folder_id , self.db.values())
        return list(iterator)
        

class InMemoryFolderRepository(AbstractRepository):
    def __init__(self) -> None:
        in_memory_db["folders"] = {}
        self.db = in_memory_db["folders"]

    def add(self, model: Model):
        self.db[model.id] = model
        return model

    def get_by_id(self, id):
        project = self.db.get(id)
        if project is None:
            raise Exception("Content not found")
        return project

    def get_by_slug(self, slug):
        iterator =  filter(lambda contentry: contentry.slug == slug , self.db.values())
        try:
            content = next(iterator)
            return content
        except StopIteration:
            raise Exception("Content not found")
        

# Peewee ORM

# class PeeweeBaseRepository(AbstractRepository):
#     model = None

#     def add(self, model):
#         return self.model.create(name=model.name).to_domain_model()

#     def get_by_id(self, id: str):
#         return self.model.get_by_id(id).to_domain_model()


class ProjectRepository(AbstractRepository):
    model = peewee_orm.Project

    def add(self, project: Project):
        root_folder = peewee_orm.Folder.create(name='Root')
        project = peewee_orm.Project.create(name=project.name, root_folder=root_folder) # type: peewee_orm.Project
        return project.to_domain_model()



class ContentryRepository(AbstractRepository):
    model = peewee_orm.Contentry

    def add(self, entry: Contentry):
        entry = peewee_orm.Contentry.create(name=entry.name, slug=entry.slug, folder=entry.folder.id) # type: peewee_orm.Contentry
        return entry.to_domain_model()


    def get(self, slug: str):
        entry = peewee_orm.Contentry.get(slug=slug)
        return entry.to_domain_model()