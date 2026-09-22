from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(2)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(2)
    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"
    driver.back()
    sleep (2)
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    sleep(2)
    driver.quit()

