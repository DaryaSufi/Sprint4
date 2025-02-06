import allure

from locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    @allure.step('Открываем форму для заказа по кнопке вверху страницы')
    def open_form_for_order(self):
        self.driver.find_element(*OrderPageLocators.the_order_button_at_the_top_of_the_page).click()

    @allure.step('Заполняем форму Для кого самокат и нажимаем Далее')
    def fill_for_who_form(self, name, sure_name, address_name, phone_number):
        self.driver.find_element(*OrderPageLocators.name_input_field).send_keys(name)
        self.driver.find_element(*OrderPageLocators.last_name_input_field).send_keys(sure_name)
        self.driver.find_element(*OrderPageLocators.address_input_field).send_keys(address_name)
        self.driver.find_element(*OrderPageLocators.phone_input_field).send_keys(phone_number)
        self.driver.find_element(*OrderPageLocators.the_next_button).click()

    @allure.step('Заполняем форму Про аренду и нажимаем кнопок Заказать и Да')
    def fill_form_about_rent(self, when_to_bring_the_scooter, rental_period_locator, checkbox_locator, comment):
        self.fill_form(*OrderPageLocators.when_to_bring_the_scooter, when_to_bring_the_scooter)
        self.driver.find_element(*OrderPageLocators.rental_period).click()
        self.driver.find_element(*rental_period_locator).click()
        self.driver.find_element(*checkbox_locator).click()
        self.fill_form(*OrderPageLocators.comment_for_the_courier, comment)
        self.driver.find_element(*OrderPageLocators.the_order_button_in_the_order_form).click()
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Открываем форму для заказа по кнопке внизу страницы')
    def open_form_oredr_the_order_button_at_the_bottom_of_the_page(self):
        self.driver.find_element(*OrderPageLocators.the_order_button_at_the_bottom_of_the_page).click()

    @allure.step('Проверяем, что при нажатии на логотип «Самоката», попадаем на главную страницу «Самоката».')
    def logo_samokat_click(self):
        self.driver.find_element(*OrderPageLocators.scooter_logo).click()

    @allure.step('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def logo_yandex_click(self):
        self.driver.find_element(*OrderPageLocators.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])











