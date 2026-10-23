import uuid
import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def put_project_raw(project_id, payload):
    resp = requests.put(f"{base_url}/projects/{project_id}", json=payload, headers=my_headers)
    return resp


def test_put_nonexistent_project():
    nonexistent_id = "00000000-0000-0000-0000-000000000000"
    updates = {"title": "Это обновление не должно примениться"}

    print(f"🧪 Тест: попытка обновления несуществующего проекта (ID={nonexistent_id})")

    resp = put_project_raw(nonexistent_id, updates)

    assert resp.status_code == 404, (
        f"Ожидался статус 404 для несуществующего проекта, "
        f"получен {resp.status_code}. Ответ сервера: {resp.text}"
    )
    assert len(resp.content) > 0, "Ответ сервера пуст при 404 — возможно, ошибка конфигурации API"


    print("✅ Тест пройден: API корректно вернул 404 при попытке обновить несуществующий проект")