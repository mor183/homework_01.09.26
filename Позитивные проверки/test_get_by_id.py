import uuid
import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def create_project(title):
    payload = {"title": title}
    resp = requests.post(f"{base_url}/projects", json=payload, headers=my_headers)
    resp.raise_for_status()
    data = resp.json()

    if "title" not in data and "name" in data:
        data["title"] = data["name"]
    return data


def get_project_by_id(project_id):
    resp = requests.get(f"{base_url}/projects/{project_id}", headers=my_headers)
    resp.raise_for_status()
    return resp.json()


def delete_project(project_id):
    resp = requests.delete(f"{base_url}/projects/{project_id}", headers=my_headers)
    if resp.status_code not in (200, 201, 204):
        resp.raise_for_status()


def test_get_project_by_id():
    title = f"Autotest-get-{uuid.uuid4().hex[:8]}"
    project = None

    try:
        project = create_project(title)
        print(f" Проект создан: id={project['id']}, title={project.get('title')}")

        fetched_project = get_project_by_id(project["id"])
        print(" Ответ сервера на GET /projects/{id}:", fetched_project)

        assert "id" in fetched_project, "В ответе нет поля id"
        assert fetched_project["id"] == project["id"], "ID в ответе не совпадает с созданным"

        found_title = fetched_project.get("title") or fetched_project.get("name")
        assert found_title == title, f"Название не совпадает: ожидалось '{title}', получено '{found_title}'"

        print(" Проверка пройдена: проект корректно получен по ID")

    finally:

        if project is not None and "id" in project:
            try:
                delete_project(project["id"])
                print(f" Тестовый проект {project['id']} удалён")
            except Exception as e:
                print(f" Не удалось удалить тестовый проект: {e}")