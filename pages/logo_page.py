import allure

from locator.logo_locators import LogoLocators
from pages.base_page import BasePage


class LogoPage(BasePage):

    @allure.step('Нажимаем на лого яндекс переключение окон получаем урлс')
    def click_on_yandex_logo(self):
        self.press_on_text_by_locator(LogoLocators.YANDEX_LOGO)
        self.select_new_tab()
        return self.get_current_urls()

    @allure.step('Нажимаем на лого самокат получаем урлс главной страницы')
    def click_on_logo_samokat(self):
        self.press_on_text_by_locator(LogoLocators.SAMOCAT_LOGO)
        return self.get_current_urls()