import allure

from locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from constants import Constants


class TestOrderPage:

    @allure.step
    def tets_place_an_order(self,driver):
        driver.find_element(OrderPageLocators.the_order_button_at_the_top_of_the_page).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        driver.find_element(OrderPageLocators.name_input_field).send_key(Constants.NAME1)
        driver.find_element(OrderPageLocators.last_name_input_field).send_key(Constants.SURNAME1)
        driver.find_element(OrderPageLocators.address_input_field).send_key(Constants.ADDRESS1)
        driver.find_element(OrderPageLocators.metro_station).click()
        driver.find_element(By.XPATH, ".//*[text() = 'Сокольники']").click()
        driver.find_element(OrderPageLocators.phone_input_field).send_key(Constants.PHONE1)
        driver.find_element(OrderPageLocators.the_next_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        driver.find_element(OrderPageLocators.when_to_bring_the_scooter).send_key(Constants.DATA1)
        driver.find_element(OrderPageLocators.rental_period).click()
        driver.find_element(By.XPATH, ".//*[text() = 'Двое суток']").click()
        driver.find_element(OrderPageLocators.checkbox_blak).click()
        driver.find_element(OrderPageLocators.comment_for_the_courier).send_key(Constants.COMMENT1)
        driver.find_element(OrderPageLocators.the_order_button_in_the_order_form).click()
        driver.find_element(OrderPageLocators.yes_button).click()
        assert driver.find_eltment(OrderPageLocators.order_registration)
        driver.find_element(OrderPageLocators.view_the_status).click()
        driver.find_element(OrderPageLocators.scooter_logo).click()
        assert driver.current_url == Constants.URL
        driver.find_element(OrderPageLocators.yandex_logo).click()
        assert driver.current_url == Constants.URL_DZEN

    @allure.step
    def test_place_an_order_other_data(self):
        self.driver.find_element(OrderPageLocators.the_order_button_at_the_bottom_of_the_page).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        self.driver.find_element(OrderPageLocators.name_input_field).send_key(Constants.NAME2)
        self.driver.find_element(OrderPageLocators.last_name_input_field).send_key(Constants.SURNAME2)
        self.driver.find_element(OrderPageLocators.address_input_field).send_key(Constants.ADDRESS2)
        self.driver.find_element(OrderPageLocators.metro_station).click()
        self.driver.find_element(By.XPATH, ".//*[text() = 'Лубянка']").click()
        self.driver.find_element(OrderPageLocators.phone_input_field).send_key(Constants.PHONE2)
        self.driver.find_element(OrderPageLocators.the_next_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        self.driver.find_element(OrderPageLocators.when_to_bring_the_scooter).send_key(Constants.DATA2)
        self.driver.find_element(OrderPageLocators.rental_period).click()
        self.driver.find_element(By.XPATH, ".//*[text() = 'Трое суток']").click()
        self.driver.find_element(OrderPageLocators.checkbox_blak).click()
        self.driver.find_element(OrderPageLocators.comment_for_the_courier).send_key(Constants.COMMENT2)
        self.driver.find_element(OrderPageLocators.the_order_button_in_the_order_form).click()
        self.driver.find_element(OrderPageLocators.yes_button).click()
        assert driver.find_eltment(OrderPageLocators.order_registration)
        driver.find_element(OrderPageLocators.view_the_status).click()
        driver.find_element(OrderPageLocators.scooter_logo).click()
        assert driver.current_url == Constants.URL
        driver.find_element(OrderPageLocators.yandex_logo).click()
        assert driver.current_url == Constants.URL_DZEN
