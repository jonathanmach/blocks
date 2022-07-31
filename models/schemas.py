from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Str()
    title = fields.Str()

class FolderSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    slug = fields.Str()
    parent_id = fields.Str()


class ContentSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    parent_id = fields.Str()
    slug = fields.Str()
    data = fields.Dict()
