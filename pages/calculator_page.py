from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_delay_value(self, delay_value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    def click_operator_button(self, operator):
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    def click_equals_button(self):
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    def get_result_text(self):
        element = WebDriverWait(self.driver, 46).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.screen"))
            )
        WebDriverWait(self.driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
            )
        assert "15" in element.text, f"Ожидаемый текст не найден: {element.text}"
       
    
