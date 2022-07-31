def test_tdd(test_client):
    project_payload = {"name": "Company Website"}
    response = test_client.post("/projects", json=project_payload)
    assert response.status_code == 201
    project_id = response.json["id"]

    # Get project by id
    response = test_client.get(f"/projects/{project_id}")
    assert response.status_code == 200

    # Add contentry to project
    content_data = {
        "main_nav": [],
        "is_right_to_left": False,
        "footer_nav": [],
        "footer_copyright": "© 2022 TechMastery",
    }
    content_payload = {"title": "Company Website", "slug": "site-settings", "data": content_data}
    response = test_client.post(f"/projects/{project_id}/content", json=content_payload)
    assert response.status_code == 201

    # Fetch contentry by slug
    response = test_client.get(f"/content/site-settings")
    assert response.status_code == 200

def test_get_content_list_by_folder(test_client):
    """GIVEN a Project and a `blogposts` folder"""
    project_payload = {"title": "Company Website"}
    response = test_client.post("/projects", json=project_payload)
    assert response.status_code == 201
    project_id = response.json["id"]

    # Add a folder to the project
    folder_payload = {"name": "blogposts"}
    response = test_client.post("/folders", json=folder_payload)
    assert response.status_code == 201
    folder_id = response.json["id"]

    # Add content to the folder
    content_payload = {"title": "Blogpost #1", "slug": "blog-1", "parent_id":folder_id, "data": {}}
    response = test_client.post(f"/projects/{project_id}/content", json=content_payload)
    content_payload = {"title": "Blogpost #2", "slug": "blog-2", "parent_id":folder_id, "data": {}}
    response = test_client.post(f"/projects/{project_id}/content", json=content_payload)
    content_payload = {"title": "Blogpost #3", "slug": "blog-3", "parent_id":folder_id, "data": {}}
    response = test_client.post(f"/projects/{project_id}/content", json=content_payload)

    # Get the content list by folder
    response = test_client.get(f"/projects/{project_id}/folders/{folder_id}/content")
    assert response.status_code == 200
    assert len(response.json) == 3