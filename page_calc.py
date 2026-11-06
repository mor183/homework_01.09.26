import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    with allure.step("Ввод ожидания"):
        """Выставляем ожидание калькулятора необходимое для получения результата основных арифметических операций - 2 секунды"""
        def delay(self):
            delay_field = self._driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
            delay_field.clear()
            delay_field.send_keys('2')

    with allure.step("Выполнение выражения"):
        """Выполняем вычисление выражения 7 + 8 = 15"""
        def sum_nums(self):
            self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[1]').click()
            self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[4]').click()
            self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[2]').click()
            self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[15]').click()

    with allure.step("Сравнение результата со значением 15"):
        """Сравниваем результат, полученный в ходе вычисление с ожидаемым результатом."""
        def result(self):
            wait = WebDriverWait(self._driver, 4)
            wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, '[class = "screen"]'), '15'))
            return self._driver.find_element(By.CSS_SELECTOR, '[class = "screen"]').text

    with allure.step("Закрытие браузера Chrome"):
        def close_driver(self):
            self._driver.quit()
