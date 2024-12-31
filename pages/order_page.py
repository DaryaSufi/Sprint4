from locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from conftest import driver
from constants import Constants

class OrderPage:
    the_order_button_at_the_top_of_the_page = OrderPageLocators.the_order_button_at_the_bottom_of_the_page
    the_order_button_at_the_bottom_of_the_page = OrderPageLocators.the_order_button_at_the_bottom_of_the_page
    name_input_field = OrderPageLocators.name_input_field
    last_name_input_field = OrderPageLocators.last_name_input_field
    address_input_field = OrderPageLocators.address_input_field
    metro_station = OrderPageLocators.metro_station
    phone_input_field = OrderPageLocators.phone_input_field
    the_next_button = OrderPageLocators.the_next_button
    when_to_bring_the_scooter = OrderPageLocators.when_to_bring_the_scooter
    rental_period = OrderPageLocators.rental_period
    scooter_color = OrderPageLocators.scooter_color
    comment_for_the_courier = OrderPageLocators.comment_for_the_courier
    the_order_button_in_the_order_form = OrderPageLocators.the_order_button_in_the_order_form
    yes_button = OrderPageLocators.yes_button
    order_registration = OrderPageLocators.order_registration

    def __init__(self,driver):
        self.driver = driver
    def place_an_order(self):
        self.driver.find_element(OrderPageLocators.the_order_button_at_the_top_of_the_page).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        self.driver.find_element(OrderPageLocators.name_input_field).send_key(Constants.NAME1)
        self.driver.find_element(OrderPageLocators.last_name_input_field).send_key(Constants.SURNAME1)
        self.driver.find_element(OrderPageLocators.address_input_field).send_key(Constants.ADDRESS1)
        self.driver.find_element(OrderPageLocators.metro_station).click()
        self.driver.find_element(By.XPATH, ".//*[text() = 'Сокольники']").click()
        self.driver.find_element(OrderPageLocators.phone_input_field).send_key(Constants.PHONE1)
        self.driver.find_element(OrderPageLocators.the_next_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
        self.driver.find_element(OrderPageLocators.when_to_bring_the_scooter).send_key(Constants.DATA1)
        self.driver.find_element(OrderPageLocators.rental_period).click()
        self.driver.find_element(By.XPATH, ".//*[text() = 'Двое суток']").click()
        self.driver.find_element(OrderPageLocators.checkbox_blak).click()
        self.driver.find_element(OrderPageLocators.comment_for_the_courier).send_key(Constants.COMMENT1)
        self.driver.find_element(OrderPageLocators.the_order_button_in_the_order_form).click()
        self.driver.find_element(OrderPageLocators.yes_button).click()

    def place_an_order_other_data(self):
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





