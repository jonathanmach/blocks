from peewee import Model, CharField, DateTimeField, ForeignKeyField
from datetime import datetime as dt
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField
import shortuuid
import models as domain_models

db = SqliteExtDatabase(
    database="test.db",
    pragmas=(("foreign_keys", 1),),  # Enforce foreign-key constraints.
)


class BaseModel(Model):
    id = CharField(primary_key=True, default=lambda: shortuuid.uuid())
    created_at = DateTimeField(default=lambda: dt.now())
    updated_at = DateTimeField(default=lambda: dt.now())

    def save(self, *args, **kwargs):
        self.updated_at = dt.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def save_no_update(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db


class Folder(BaseModel):
    name = CharField(null=True)

    def to_domain_model(self) -> domain_models.Folder:
        folder = domain_models.Folder(self.name)
        folder.id = self.id
        return folder


class Project(BaseModel):
    name = CharField(null=True)
    root_folder = ForeignKeyField(Folder)

    def to_domain_model(self) -> domain_models.Project:
        project = domain_models.Project(self.name)
        project.id = self.id
        project.root_folder = self.root_folder.to_domain_model()
        return project


class Contentry(BaseModel):
    name = CharField(null=True)
    slug = CharField(null=True)
    folder = ForeignKeyField(Folder)
    data = JSONField(default=dict)

    def to_domain_model(self) -> domain_models.Contentry:
        folder = self.folder.to_domain_model()
        page = domain_models.Contentry(self.name, self.slug, folder)
        page.id = self.id
        return page


def create_tables():
    with db:
        db.create_tables([Project, Contentry, Folder], safe=True)


create_tables()
