import allure

from locator.logo_locators import LogoLocators
from pages.base_page import GeneralMethods


class LogoPage(GeneralMethods):

    @allure.step('Нажимаем на лого яндекс получаем урлс')
    def click_on_yandex_logo(self):
        self.press_on_text_by_locator(LogoLocators.YANDEX_LOGO)
        return self.get_current_urls()

    @allure.step('Нажимаем на лого самокат получаем урлс главной страницы')
    def click_on_logo_samokat(self):
        self.press_on_text_by_locator(LogoLocators.SAMOCAT_LOGO)
        return self.get_current_urls()