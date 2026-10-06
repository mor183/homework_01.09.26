import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_form ():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    driver.get ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name=address]").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
    )

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    
    green_highlighted = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted) == 9 
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    
    green_highlighted = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted) == 9  

    driver.quit()


