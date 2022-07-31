from flask import Blueprint, jsonify, request
from models import Project
from models.base import Contentry, Folder
from models.schemas import FolderSchema, ProjectSchema, ContentSchema
import repository

project_api = Blueprint("project_api", __name__)

project_repo = repository.InMemoryProjectRepository()
contentry_repo = repository.InMemoryContentRepository()
folder_repo = repository.InMemoryFolderRepository()


@project_api.route("/projects", methods=["POST"])
def create_project():
    payload = request.get_json()
    project = Project(payload["title"])

    # Parse the request body
    project = project_repo.add(project)
    response = ProjectSchema().dump(project)
    return response, 201


@project_api.route("/projects/<project_id>", methods=["GET"])
def get_project(project_id):
    project = project_repo.get_by_id(project_id)
    response = ProjectSchema().dump(project)
    return response, 200


@project_api.route("/folders", methods=["POST"])
def create_folder():
    project_id = 'xyz'  # TODO: Get from jwt token
    payload = request.get_json()
    entry = Folder(payload["name"], payload.get("slug"), payload.get("parent_id"))
    entry = folder_repo.add(entry)

    response = FolderSchema().dump(entry)
    return response, 201

@project_api.route("/projects/<project_id>/content", methods=["POST"])
def create_content(project_id):
    payload = request.get_json()
    entry = Contentry(payload["title"], payload.get("slug"), payload.get("data"), payload.get("parent_id"))
    entry = contentry_repo.add(entry)

    response = ContentSchema().dump(entry)
    return response, 201


@project_api.route("/content/<slug>", methods=["GET"])
def get_content_by_slug(slug):
    entry = contentry_repo.get_by_slug(slug)
    response = ContentSchema().dump(entry)
    return response, 200

@project_api.route("/projects/<project_id>/folders/<folder_id>/content", methods=["GET"])
def get_content_by_folder(project_id, folder_id):
    entries = contentry_repo.get_by_folder(folder_id)
    response = ContentSchema(many=True).dump(entries)
    return jsonify(response), 200
