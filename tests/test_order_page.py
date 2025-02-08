import allure
import pytest
from locators import OrderPageLocators
from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверяем оформление заказа по кнопке вверху страницы')
    @pytest.mark.parametrize('data', [
        {
            'name': 'Федор',
            'sure_name': 'Федоров',
            'address': 'ул.Пятницкая, д.35',
            'metro': 'Лубянка',
            'phone': '89607667147',
            'date': '06.02.2025',
            'period': OrderPageLocators.dvoe_sutok,
            'color': OrderPageLocators.checkbox_blak,
            'comment': 'Комментарий 1'
        },
        {
            'name': 'Петр',
            'sure_name': 'Петров',
            'address': 'ул.Остоженка, д.49',
            'metro': 'Лубянка',
            'phone': '89628778158',
            'date': '07.02.2025',
            'period': OrderPageLocators.troe_sutok,
            'color': OrderPageLocators.checkbox_grey,
            'comment': 'Комментарий 2'
         }])
    def test_full_order_process(self, driver, data):
        order_page = OrderPage(driver)
        order_page.go_to_site()

        order_page.open_form_for_order()

        order_page.fill_for_who_form(
            data['name'],
            data['sure_name'],
            data['address'],
            data['metro'],
            data['phone']
        )

        order_page.fill_form_about_rent(
            data['date'],
            data['period'],
            data['color'],
            data['comment']
        )

        assert order_page.is_order_confirmed()

    @allure.title("Проверка открытия формы для заказа по кнопке внизу страницы")
    def test_open_form_oredr_the_order_button_at_the_bottom_of_the_page(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.open_form_order_the_order_button_at_the_bottom_of_the_page()
        assert order_page.is_element_visible(OrderPageLocators.order_registration)

    @allure.title("Проверка клика по логотипу самокат")
    def test_logo_samokat_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_samokat_click()
        order_page.get_current_url()
        assert order_page.get_current_url() == Constants.URL

    @allure.title("Проверка клика по логотипу яндекс")
    def test_logo_yandex_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_yandex_click()
        assert order_page.get_tab_and_switch() == Constants.URL_DZEN
