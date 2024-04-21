import time

import allure

from pages.logo_page import LogoPage


class TestLogo:

    @allure.title("Проверка логотипа яндекс")
    @allure.description("Входим на главную страницу кликаем по логотипу яндекс получаем урл страницы")
    def test_check_open_yandex_dzen(self, driver):
        home_page = LogoPage(driver)
        assert home_page.click_on_yandex_logo() == 'https://dzen.ru/?yredirect=true'

    @allure.title("Проверка логина самолета")
    @allure.description("Открываем страницу заказа нажимаем на логотип самолета проверяем урл главной страницы")
    def test_check_logo_samocat(self, get_to_order_page):
        home_page = LogoPage(get_to_order_page)
        assert home_page.click_on_logo_samokat() == 'https://qa-scooter.praktikum-services.ru/'


