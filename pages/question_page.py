import allure
from selenium.webdriver.common.by import By

from locator.locator_questions_page import QuestionsLocators
from pages.base_page import BasePage


class QuestionPage(BasePage):

    @allure.step('Выбор вопроса и нажатие')
    def click_question(self, locator_question):
        self.select_locxcator_by_id(locator_question)

    @allure.step('Возврат текста ответа ')
    def return_text(self, locator):
        return self.get_text(locator)

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text_of_question(self, locator_question):
        self.click_question(locator_question)



