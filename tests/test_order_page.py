import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from locators import OrderPageLocators
from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверяем заполнение формы Для кого самокат')
    @pytest.mark.parametrize('data', [
        {
            'name': 'Федор',
            'sure_name': 'Федоров',
            'address': 'ул.Пятницкая, д.35',
            'metro': OrderPageLocators.metro_sokolniki,
            'phone': '89607667147',
            'date': '2025-05-01',
            'period': OrderPageLocators.dvoe_sutok,
            'color': OrderPageLocators.checkbox_blak,
            'comment': 'Комментарий 1'
        },
        {
            'name': 'Петр',
            'sure_name': 'Петров',
            'address_name': 'ул.Остоженка, д.49',
            'metro': OrderPageLocators.metro_lubyanka,
            'phone_number': '89628778158',
            'date': '06.01.2025',
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

    @allure.title("Проверка клика по логотипу самокат")
    def test_logo_samokat_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.logo_samokat_click()
        assert order_page.current_url == Constants.URL

    @allure.title("Проверка клика по логотипу яндекс")

    def test_logo_yandex_click(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()

        main_window = driver.current_window_handle
        order_page.logo_yandex_click()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

        assert Constants.URL_DZEN in driver.current_url
        driver.close()
        driver.switch_to.window(main_window)