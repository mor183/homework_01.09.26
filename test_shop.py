import pytest
from selenium import webdriver
from pages.shop_page import LoginPage, ProductsPage, CheckoutPage, PersonalInfoPage, OverviewPage

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_complete_purchase(browser):
    saucedemo_url = "https://www.saucedemo.com/"

    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = CheckoutPage(browser)
    personal_info_page = PersonalInfoPage(browser)
    overview_page = OverviewPage(browser)

    login_page.login_as_standard_user()

    products_page.add_products_to_cart("Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")

    products_page.go_to_shopping_cart()

    checkout_page.proceed_to_checkout()

    personal_info_page.fill_personal_info("Anna", "K", "1234")

    total_amount = overview_page.get_total_amount()
    assert total_amount == "58.29", f"Expected '58.29', but got {total_amount}"

    overview_page.complete_purchase()