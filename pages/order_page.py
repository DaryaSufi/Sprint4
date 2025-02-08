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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderPageLocators.the_order_button_at_the_top_of_the_page)))
        self.driver.find_element(*OrderPageLocators.the_order_button_at_the_top_of_the_page).click()

    @allure.step('Заполняем форму Для кого самокат и нажимаем Далее')
    def fill_for_who_form(self, name, sure_name, address_name, metro, phone_number):
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.name_input_field))
        self.fill_form(OrderPageLocators.name_input_field, name)
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.last_name_input_field))
        self.fill_form(OrderPageLocators.last_name_input_field, sure_name)
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.address_input_field))
        self.fill_form(OrderPageLocators.address_input_field, address_name)
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.metro_station))
        self.fill_form(OrderPageLocators.metro_station, metro)
        self.driver.find_element(*OrderPageLocators.metro_lubyanka).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.phone_input_field))
        self.fill_form(OrderPageLocators.phone_input_field, phone_number)
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.cookie_button))
        self.driver.find_element(*OrderPageLocators.cookie_button).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.the_next_button))
        self.driver.find_element(*OrderPageLocators.the_next_button).click()

    @allure.step('Заполняем форму Про аренду и нажимаем кнопок Заказать и Да')
    def fill_form_about_rent(self, when_to_bring_the_scooter, rental_period_locator, checkbox_locator, comment):
         self.driver.find_element(*OrderPageLocators.when_to_bring_the_scooter).click()
         self.fill_form(OrderPageLocators.scooter_date_input, when_to_bring_the_scooter)
         self.driver.find_element(*OrderPageLocators.scot_date_input).click()
         WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.rental_period))
         self.driver.find_element(*OrderPageLocators.rental_period).click()
         WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.rental_period_menu))
         self.driver.find_element(*rental_period_locator).click()
         self.driver.find_element(*checkbox_locator).click()
         self.driver.find_element(*OrderPageLocators.comment_for_the_courier).click()
         self.fill_form(OrderPageLocators.comment_for_the_courier,comment)
         self.driver.find_element(*OrderPageLocators.the_order_button_in_the_order_form).click()
         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(OrderPageLocators.yes_button))
         self.driver.find_element(*OrderPageLocators.yes_button).click()


    @allure.step('Открываем форму для заказа по кнопке внизу страницы')
    def open_form_order_the_order_button_at_the_bottom_of_the_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.the_order_button_at_the_bottom_of_the_page))
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.cookie_button))
        self.driver.find_element(*OrderPageLocators.cookie_button).click()
        self.driver.find_element(*OrderPageLocators.the_order_button_at_the_bottom_of_the_page).click()

    @allure.step('Проверяем, что при нажатии на логотип «Самоката», попадаем на главную страницу «Самоката».')
    def logo_samokat_click(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.cookie_button))
        self.driver.find_element(*OrderPageLocators.cookie_button).click()
        self.driver.find_element(*OrderPageLocators.scooter_logo).click()

    @allure.step('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def logo_yandex_click(self):
        self.driver.find_element(*OrderPageLocators.yandex_logo).click()