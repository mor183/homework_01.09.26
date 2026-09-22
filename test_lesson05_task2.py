from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    driver.find_element(By.NAME, "custname").click()
    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys ("Ann")
    sleep (4)

    driver.find_element(By.XPATH, "//button[contains(text(),'Submit order')]").click()
    sleep(2)

    driver.current_url == "https://httpbin.qa-territory.online/post"
    sleep(2)

    driver.quit()

