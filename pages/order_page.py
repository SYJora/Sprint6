import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator.order_locator_page import OrderPageLocator
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Нажатие на кнопку заказать самокат')
    def click_button_order(self, flag):
        if flag == 's':
            self.press_on_text_by_locator(OrderPageLocator.BUTTON_ORDER)
        else:
            self.press_on_text_by_locator(OrderPageLocator.BUTTON_COOKES)
            self.press_on_text_by_locator(OrderPageLocator.BUTTON_ORDER_BIG)

    @allure.step('Выбор станций метро')
    def select_metro(self):
        self.press_on_text_by_locator(OrderPageLocator.METRO)
        self.press_on_text_by_locator(OrderPageLocator.STANTION)

    @allure.step('Выбор дня доставки')
    def select_deliveri_day(self):
        self.press_on_text_by_locator(OrderPageLocator.DATA)
        self.press_on_text_by_locator(OrderPageLocator.DATA_DELIVERY)

    @allure.step('Выбрать количество дней аренды')
    def select_data_rent(self):
        self.press_on_text_by_locator(OrderPageLocator.RENT_DATA_PLACEHOLDER)
        self.press_on_text_by_locator(OrderPageLocator.RENT_DAY)

    @allure.step('Ожидание окна подтверждаешего аренды')
    def finish_order(self):
        self.wait_element_visabiliti_all_element(OrderPageLocator.SUCCESSFUL_ORDER)


    @allure.step('Заполнение первой страницы для заказа самоката. Заполняем поля Имя,Фамилия,Адрес,Телефон')
    def enter_order_param(self, name, lastname, adres, phone, s):
        self.click_button_order(s)
        self.find_and_sed(OrderPageLocator.NAME, name)
        self.find_and_sed(OrderPageLocator.LASTNAME, lastname)
        self.find_and_sed(OrderPageLocator.ADRES, adres)
        self.select_metro()
        self.find_and_sed(OrderPageLocator.PHONE, phone)
        self.press_on_text_by_locator(OrderPageLocator.BUTTON_NEXT)

    @allure.step('Заполнение страницы для заказа самоката. Заполняем Дату доставки, Время оренды, потверждаем заказ')
    def second_page_enter_param(self, comment):
        self.select_deliveri_day()
        self.select_data_rent()
        self.press_on_text_by_locator(OrderPageLocator.COLOR_SELECT)
        self.find_and_sed(OrderPageLocator.COMMENT, comment)
        self.press_on_text_by_locator(OrderPageLocator.BUTTON_ORDER_LAST_PAGE)
        self.press_on_text_by_locator(OrderPageLocator.BUTTON_YES)



