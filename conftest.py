import allure
import pytest
from selenium import webdriver

@allure.step("Открываем главную страницу самоката")
@pytest.fixture(scope = 'function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    firefox_driver.get('https://qa-scooter.praktikum-services.ru/')
    yield firefox_driver
    firefox_driver.quit()

@allure.step("Открываем страницу заполнения бланка на заказ самоката")
@pytest.fixture(scope = 'function')
def get_to_order_page():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    firefox_driver.get('https://qa-scooter.praktikum-services.ru/order')
    yield firefox_driver
    firefox_driver.quit()