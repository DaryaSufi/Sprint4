import allure
import pytest

from locators import ImportantQuestionsLocators
from pages.base_page import BasePage


class ImportantQuestions(BasePage):
    def __init__(self,driver):
        self.driver=driver

    @allure.step('Кликаем по строке Сколько это стоит')
    def click_how_much_does_it_cost(self):
        self.driver.find_element(ImportantQuestionsLocators.how_much_does_it_cost).click()

    @allure.step('Кликаем по строке Хочу сразу несколько самокатов')
    def click_i_want_some_scooters(self):
        self.driver.find_element(ImportantQuestionsLocators.i_want_some_scooters).click()

    @allure.step('Кликаем по строке Как рассчитывается время аренды?')
    def click_how_is_the_rental_time_calculated(self):
        self.driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated).click()

    @allure.step('Кликаем по строке Можно ли заказать самокат прямо на сегодня?')
    def click_can_i_order_a_scooter_for_today(self):
        self.driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today).click()

    @allure.step('Кликаем поо строке Можно ли продлить заказ или вернуть самокат раньше?')
    def click_is_it_possible_to_extend_the_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order).click()

    @allure.step('Кликаем по строке Вы привозите зарядку вместе с самокатом?')
    def click_do_you_bring_charger(self):
        self.driver.find_element(ImportantQuestionsLocators.do_you_bring_charger).click()

    @allure.step('Кликаем по строке Можно ли отменить заказ?')
    def click_is_it_possible_to_cancel_an_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_cancel_an_order).click()

    @allure.step('Кликаем по строке Я жизу за МКАДом, привезёте?')
    def click_i_live_beyond_the_MKAD(self):
        self.driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD).click()
