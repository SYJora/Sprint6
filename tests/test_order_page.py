import allure
import pytest

from data import DataTest
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Позетивный сценарий на заказ самоката")
    @allure.description("Выполняем полное прохождения позитивного сценария с двумя наборами данных")
    @pytest.mark.parametrize('data', [
        *DataTest.Order1,
        *DataTest.Order2
    ])
    def test_make_order_page(self, driver, data):
        name, lastname, adres, phone, s, comment = data
        make_order = OrderPage(driver)
        make_order.enter_order_param(name, lastname, adres, phone, s)
        make_order.second_page_enter_param(comment)
        assert make_order.finish_order() ==  True

