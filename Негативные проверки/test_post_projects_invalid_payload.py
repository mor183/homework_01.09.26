import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def post_projects_raw(payload):
    resp = requests.post(f"{base_url}/projects", json=payload, headers=my_headers)
    return resp


def test_post_project_without_title():
    payload_empty = {}
    
    print("Тест: создание проекта без заголовка (пустой payload)")
    resp_empty = post_projects_raw(payload_empty)
    assert resp_empty.status_code == 400, (
        f"Ожидался статус 400 для пустого payload, получен {resp_empty.status_code}. "
        f"Ответ: {resp_empty.text}"
    )

    print("Тест пройден: API корректно отверг все некорректные payload с ошибкой 400")