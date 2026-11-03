import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page_shop import BuyingPage

@allure.title("Проверка итоговой стоимости в интернет-магазине")
@allure.description("Тест сравнивает сумму добавленных в корзину товаров с конкретным значением")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_buying_process():
    with allure.step("Запуск браузера FireFox"):
        options = Options()
        options.binary_location = r"C:\Users\mor18\.cache\selenium\firefox\win64\157.0.1\firefox.exe"
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)

    with allure.step("Переход на страницу интернет-магазина"):
        page = BuyingPage(browser)

    with allure.step("Авторизация"):
        page.authorization("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
        page.add_products()
    
    with allure.step("Переход в корзину"):
        page.go_to_cart()

    with allure.step("Ввод данных покупателя"):
        page.personal_data("Аnna", "K", "1234")
    
    with allure.step("Сравнение итоговой стоимости с конкретным значением"):
        total = page.total_cost()
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29' but got '{total}'"
    
    page.close()