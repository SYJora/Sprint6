from selenium.webdriver.common.by import By


class LogoLocators:

    YANDEX_LOGO = (By.XPATH, "//a[@href = '//yandex.ru']")
    SAMOCAT_LOGO = (By.XPATH, "//a[@href = '/']")