import pytest
from selenium.webdriver.common.by import By


class QuestionsLocators:

    question_answer = [
        pytest.param(('accordion__heading-0', "//div[@aria-labelledby = 'accordion__heading-0']/child::*"), id = 'Сколько это стоит? И как оплатить?, Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ('accordion__heading-1', "//div[@aria-labelledby = 'accordion__heading-1']/child::*"),
        ('accordion__heading-2', "//div[@aria-labelledby = 'accordion__heading-2']/child::*"),
        ('accordion__heading-3', "//div[@aria-labelledby = 'accordion__heading-3']/child::*"),
        ('accordion__heading-4', "//div[@aria-labelledby = 'accordion__heading-4']/child::*"),
        ('accordion__heading-5', "//div[@aria-labelledby = 'accordion__heading-5']/child::*"),
        ('accordion__heading-6', "//div[@aria-labelledby = 'accordion__heading-6']/child::*"),
        ('accordion__heading-7', "//div[@aria-labelledby = 'accordion__heading-7']/child::*")
    ]