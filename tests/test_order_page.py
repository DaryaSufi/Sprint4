import allure

from locators import OrderPageLocators
from conftest import driver
from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Проверка оформления заказа с 1-м набором данных")
    def test_place_an_order(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.place_an_order()
        assert driver.find_eltment(OrderPageLocators.order_registration)

    @allure.title("Проверка клика по логотипу самокат")
    def test_logo_samokat_click(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_samokat_click()
        assert driver.current_url == Constants.URL

    @allure.title("Проверка клика по логотипу яндекс")
    def test_logo_yandex_click(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_yandex_click()
        assert driver.current_url == Constants.URL_DZEN

    @allure.title("Проверка оформления заказа со 2-м набором данных")
    def test_place_an_order_other_data(self):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.place_an_order_other_data()
        assert driver.find_eltment(OrderPageLocators.order_registration)
