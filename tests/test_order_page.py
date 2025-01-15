import allure

from locators import OrderPageLocators
from conftest import driver
from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title
    def test_place_an_order(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.place_an_order
        assert driver.find_eltment(OrderPageLocators.order_registration)
        driver.find_element(OrderPageLocators.view_the_status).click()
        driver.find_element(OrderPageLocators.scooter_logo).click()
        assert driver.current_url == Constants.URL
        driver.find_element(OrderPageLocators.yandex_logo).click()
        assert driver.current_url == Constants.URL_DZEN

    @allure.title
    def test_place_an_order_other_data(self):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.place_an_order_other_data
        assert driver.find_eltment(OrderPageLocators.order_registration)
        driver.find_element(OrderPageLocators.view_the_status).click()
        driver.find_element(OrderPageLocators.scooter_logo).click()
        assert driver.current_url == Constants.URL
        driver.find_element(OrderPageLocators.yandex_logo).click()
        assert driver.current_url == Constants.URL_DZEN
