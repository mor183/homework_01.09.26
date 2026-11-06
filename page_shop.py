import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class BuyingPage:

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)

    @allure.step("Авторизация пользователя {name}:{password}")
    def authorization(self, name: str, password: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Добавление товаров в корзину, запись общей стоимости в переменную")
    def add_products(self) -> str:
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        counter = 'Total: $58.29'
        return counter

    @allure.step("Переход в корзину")    
    def go_to_cart(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()

    @allure.step("Ввод данных покупателя")
    def personal_data(self, name: str, last_name: str, postal_code: str) -> None:
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Текст общей стоимости записываем в переменную txt")
    def total_cost(self)  -> str:
        txt = WebDriverWait(self._driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.summary_total_label'))).text
        return txt

    @allure.step("Закрытие браузера FireFox")
    def close(self)  -> None:
        self._driver.find_element(By.ID, "finish").click()
        self._driver.quit()