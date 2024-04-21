from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class GeneralMethods:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_elemebt(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def press_on_text_by_locator(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element(locator, text))

    def wait_element_displaed(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_all_elements_located(By.ID, locator))

    def find_and_sed(self, locator, values):
        self.driver.find_element(*locator).send_keys(values)

    def get_current_urls(self):
        return self.driver.current_url