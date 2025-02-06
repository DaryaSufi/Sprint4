import allure
import pytest

from locators import OrderPageLocators
from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверяем открытие формы для заказа по кнопке вверху страницы')
    def test_open_form_for_order(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.open_form_for_order()
        assert order_page.find_element(OrderPageLocators.order_registration_form) is not None

    @pytest.mark.parametrize('data', [
                {'name': 'Федор', 'sure_name': 'Федоров', 'address_name': 'ул.Пятницкая, д.35', 'phone_number':'89607667147'},
                {'name': 'Петр', 'sure_name': 'Петров', 'address_name': 'ул.Остоженка, д.49', 'phone_number': '89628778158'}
    ])
    @allure.title('Проверяем заполнение формы Для кого самокат и нажатие кнопки Далее')
    def test_fill_for_who_form(self, driver, data):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.open_form_for_order()
        order_page.fill_for_who_form(data['name'], data['sure_name'], data['address_name'], data['phone_number'])
        assert order_page.find_element(OrderPageLocators.when_to_bring_the_scooter) is not None

    @pytest.mark.parametrize('data_1', [
        (
                {'when_to_bring_the_scooter': '05.01.2025', 'rental_period_locator': OrderPageLocators.dvoe_sutok,
                 'checkbox_locator': OrderPageLocators.checkbox_blak, 'comment': 'Коментарий 1'},
        ),
        (
                {'when_to_bring_the_scooter': '06.01.2025', 'rental_period_locator': OrderPageLocators.troe_sutok,
                 'checkbox_locator': OrderPageLocators.checkbox_grey, 'comment': 'Коментарий 2'}
        )
    ])
    @allure.title('Проверяем заполнение формы Про аренду и нажатие кнопок Заказать и Да')
    def test_fill_form_about_rent(self, driver, data_1):
        order_page = OrderPage(driver)
        order_page.fill_form_about_rent(data_1['when_to_bring_the_scooter'], data_1['rental_period_locator'],
                                        data_1['checkbox_locator'], data_1['comment'])
        assert order_page.find_element(OrderPageLocators.order_registration)

    @allure.title("Проверка клика по логотипу самокат")
    def test_logo_samokat_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_samokat_click()
        assert driver.current_url == Constants.URL

    @allure.title("Проверка клика по логотипу яндекс")
    def test_logo_yandex_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_yandex_click()
        assert driver.current_url == Constants.URL_DZEN

