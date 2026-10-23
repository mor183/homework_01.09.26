import uuid
import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def get_project_list(params_to_add=None):
    resp = requests.get(base_url + "/projects", headers=my_headers, params=params_to_add)
    resp.raise_for_status()
    return resp.json()  # {company_id: [проекты]}


def create_project(title):
    payload = {"title": title}
    resp = requests.post(base_url + "/projects", json=payload, headers=my_headers)
    resp.raise_for_status()
    data = resp.json()
    assert "id" in data, "В ответе нет поля id"
    return data


def delete_project(project_id):
    resp = requests.delete(f"{base_url}/projects/{project_id}", headers=my_headers)
    if resp.status_code not in (200, 201):
        resp.raise_for_status()


def flatten_projects(projects_by_company):
    all_projects = []
    for company_projects in projects_by_company.values():
        if isinstance(company_projects, list):
            all_projects.extend(company_projects)
    return all_projects


def test_create_project():
    """Тест без фикстур: создаём, проверяем, удаляем через try/finally"""
    
    title = f"Autotest-{uuid.uuid4().hex[:8]}"
    project = None

    try:
        
        project = create_project(title)
        
        
        print(" Ответ API при создании:", project)

        
        expected_title = project.get("title") or project.get("name") or title
        
        print(f" Проект создан: id={project['id']}, ожидаемое название={expected_title}")

        # 2. Проверяем наличие в списке
        raw_list = get_project_list()
        flat_list = flatten_projects(raw_list)

        exists = any(p["id"] == project["id"] for p in flat_list)
        assert exists, f"Проект с id={project['id']} не найден в списке"

        matching_projects = [p for p in flat_list if p["id"] == project["id"]]
        assert len(matching_projects) == 1, "Найдено больше одного проекта с таким ID"

        found_project = matching_projects[0]
        found_title = found_project.get("title") or found_project.get("name")

        # Проверяем название только если оно реально есть в списке проектов
        if found_title is not None:
            assert found_title == expected_title, f"Название не совпадает: ожидалось '{expected_title}', получено '{found_title}'"
        else:
            print(" В списке проектов не найдено поле названия, проверка по названию пропущена (проверено только по ID).")

        print("Проверка пройдена: проект есть в списке")

    finally:
        # 3. Очистка
        if project is not None and "id" in project:
            try:
                delete_project(project["id"])
                print(f"Тестовый проект {project['id']} удалён")
            except Exception as e:
                print(f" Не удалось удалить тестовый проект: {e}")