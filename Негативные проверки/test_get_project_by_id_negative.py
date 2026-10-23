import uuid
import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_project_by_id_raw(project_id):
    resp = requests.get(f"{base_url}/projects/{project_id}", headers=my_headers)
    return resp


def test_get_project_by_id_negative():
    nonexistent_id = "00000000-0000-0000-0000-000000000000"
    
    print(f"🧪 Тест: запрос несуществующего проекта (ID={nonexistent_id})")

    resp = get_project_by_id_raw(nonexistent_id)

    assert resp.status_code == 404, (
        f"Ожидался статус 404 для несуществующего проекта, "
        f"получен {resp.status_code}. Ответ сервера: {resp.text}"
    )

    assert len(resp.content) > 0, "Ответ сервера пуст при 404 — возможно, ошибка конфигурации API"

    print(" Тест пройден: API корректно вернул 404 для несуществующего UUID")