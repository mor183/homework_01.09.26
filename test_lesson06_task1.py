from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    
    hello_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert hello_element.text == "Hello World!"
    driver.save_screenshot("screenshots/full_screen.png")
   

    driver.quit()
