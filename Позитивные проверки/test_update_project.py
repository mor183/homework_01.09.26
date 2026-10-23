import uuid
import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_project_list():
    resp = requests.get(f"{base_url}/projects", headers=my_headers)
    resp.raise_for_status()
    return resp.json()

def create_project(title):
    payload = {"title": title}
    resp = requests.post(f"{base_url}/projects", json=payload, headers=my_headers)
    resp.raise_for_status()
    data = resp.json()

    if "title" not in data and "name" in data:
        data["title"] = data["name"]
    return data

def update_project(project_id, updates):
    """Выполняет PUT. Возвращает сырой JSON ответа."""
    resp = requests.put(f"{base_url}/projects/{project_id}", json=updates, headers=my_headers)
    resp.raise_for_status()
    return resp.json()

def delete_project(project_id):
    resp = requests.delete(f"{base_url}/projects/{project_id}", headers=my_headers)
    if resp.status_code not in (200, 201, 204):
        resp.raise_for_status()

def flatten_projects(projects_by_company):
    all_projects = []
    for company_projects in projects_by_company.values():
        if isinstance(company_projects, list):
            all_projects.extend(company_projects)
    return all_projects

def test_update_project():
    original_title = f"Autotest-orig-{uuid.uuid4().hex[:8]}"
    updated_title = f"Autotest-updated-{uuid.uuid4().hex[:8]}"

    project = None
    try:
        project = create_project(original_title)
        print(f"Проект создан: id={project['id']}, title={project.get('title')}")


        updates = {"title": updated_title}
        put_response = update_project(project["id"], updates)
        

        assert "id" in put_response, "В ответе на PUT нет поля id"
        print(f" Запрос PUT выполнен успешно для проекта {put_response.get('id')}")


        raw_list = get_project_list()
        flat_list = flatten_projects(raw_list)


        matching_projects = [p for p in flat_list if p["id"] == project["id"]]
        assert len(matching_projects) == 1, "Проект не найден в списке после обновления"
        
        updated_in_list = matching_projects[0]
        found_title = updated_in_list.get("title") or updated_in_list.get("name")
        
        assert found_title == updated_title, (
            f"Название в списке не совпадает! Ожидалось '{updated_title}', "
            f"получено '{found_title}'. Возможно, обновление не применилось."
        )
        
        print(f" Проверка пройдена: в списке проектов название обновлено на '{found_title}'")

    finally:
  
        if project is not None and "id" in project:
            try:
                delete_project(project["id"])
                print(f" Тестовый проект {project['id']} удалён")
            except Exception as e:
                print(f"Не удалось удалить тестовый проект: {e}")