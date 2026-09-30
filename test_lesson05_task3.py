from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://httpbin.qa-territory.online/links/10")

    driver.find_elements (By.TAG_NAME, "a")

    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9

    all_links = driver.find_elements(By.TAG_NAME, 'a')
    for link in all_links:
        print(link.get_attribute('href'))

    first_link = links[0]
    assert "1" in first_link.text

    driver.quit()
