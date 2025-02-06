from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def go_to_site(self):
        self.driver.get(Constants.URL)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator)))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located((locator)), message=f'Not find elements {locator}')

    def fill_form(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)