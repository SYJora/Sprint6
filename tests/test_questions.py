import allure
import pytest

from locator.locator_questions_page import QuestionsLocators
from pages.question_page import QuestionPage
from data import DataTest



class TestQuestions:

    @allure.title("Проверка ответо на вопросы")
    @allure.description("Выполняется проверка отображения текста ответа на главной странице")
    @pytest.mark.parametrize('params', [*QuestionsLocators.question_answer])
    def test_check_question_and_answer(self, driver, params):
        question, answer = params
        question_page = QuestionPage(driver)
        list_answer = DataTest.ANSWERS
        question_page.scroll_to_elemebt()
        question_page.get_answer_text_of_question(question)
        assert question_page.return_text(answer) in list_answer
