import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_calc import Calculator

@allure.title("Калькулятор")
@allure.description("Проверка работы калькулятора")
@allure.feature("CREATE")
@allure.severity("blocker")




def test_calculator():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Загрузка страницы калькулятора"):
        calculator = Calculator(driver)

    with allure.step("Выставление задержки выполнения действия"):    
        calculator.delay()

    with allure.step("Выполнени выражения"):    
        calculator.sum_nums()

    with allure.step("Сравненение значения выражения с числом 15"):    
        assert calculator.result() == '15'
        
    with allure.step("Закрытие браузера Chrome"):    
        calculator.close_driver()
