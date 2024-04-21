import allure
from selenium.webdriver.common.by import By

from locator.locator_questions_page import QuestionsLocators
from pages.base_page import GeneralMethods


class QuestionPage(GeneralMethods):

    def click_question(self, locator_question):
        self.driver.find_element(By.ID, locator_question).click()

    def return_text(self, locator):
        return self.driver.find_element(By.XPATH, locator).text

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text_of_question(self, locator_question):
        self.click_question(locator_question)



