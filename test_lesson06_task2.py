from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    
    driver.get("https://gitflic.ru")
    driver.add_cookie ({
        "name": "SESSION",
        "value": "ZDhlMTAxNDAtOTIwNy00ZWVmLWFmMTctMDJmMzViM2E0MzA0",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/mor183")
    url_user1 = driver.current_url
    print ("URL user1:", url_user1)

    driver.delete_all_cookies ()
    driver.get("https://gitflic.ru")
    driver.add_cookie ({
            "name": "SESSION",
            "value": "MGQ1Y2NlYmItYTA0NC00MGNhLThjN2MtZmVlMzFhMmYwNWI4",
            "domain": "gitflic.ru"
        })
    driver.refresh()

    driver.get("https://gitflic.ru/user/wibeyura")
    url_user2 = driver.current_url
    print ("URL user2:", url_user2)

    assert url_user1 != url_user2, "URL для пользователей не различаются!"
    print("Тест пройден: URL для пользователей действительно разные.")

    driver.quit()
