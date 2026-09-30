from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    
    driver.get("https://gitflic.ru/")
    driver.add_cookie ({
        "name": "SESSION",
        "value": "ZDFmODA4NTYtODdiNC00NzQ2LWI1YTEtOTY4MGYxNzgyMjVl",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/")
    url_user1 = driver.current_url
    print ("URL user1:", url_user1)

    driver.delete_all_cookies ()
    driver.get("https://gitflic.ru/")
    driver.add_cookie ({
            "name": "SESSION",
            "value": "MDk3Y2YxNWEtMzJlMy00OTBhLWI3ZDYtNzYwOTdlMzgwMjcy",
            "domain": "gitflic.ru"
        })
    driver.refresh()

    driver.get("https://gitflic.ru/")
    url_user2 = driver.current_url
    print ("URL user2:", url_user2)

    assert url_user1 != url_user2, f"{url_user1}"

    driver.quit()
