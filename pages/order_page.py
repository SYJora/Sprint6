import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator.order_locator_page import OrderPageLocator
from pages.base_page import GeneralMethods


class OrderPage(GeneralMethods):

    def click_button_order(self, flag):
        if flag == 's':
            self.driver.find_element(*OrderPageLocator.BUTTON_ORDER).click()
        else:
            self.driver.find_element(*OrderPageLocator.BUTTON_COOKES).click()
            self.driver.find_element(*OrderPageLocator.BUTTON_ORDER_BIG).click()

    def select_metro(self):
        self.driver.find_element(*OrderPageLocator.METRO).click()
        self.driver.find_element(*OrderPageLocator.STANTION).click()

    def select_deliveri_day(self):
        self.press_on_text_by_locator(OrderPageLocator.DATA)
        self.press_on_text_by_locator(OrderPageLocator.DATA_DELIVERY)

    def select_data_rent(self):
        self.press_on_text_by_locator(OrderPageLocator.RENT_DATA_PLACEHOLDER)
        self.press_on_text_by_locator(OrderPageLocator.RENT_DAY)

    def finish_order(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_all_elements_located(OrderPageLocator.SUCCESSFUL_ORDER))
        return True

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



