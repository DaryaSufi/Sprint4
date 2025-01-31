import allure
import pytest

from locators import ImportantQuestionsLocators
from pages.important_questions_page import ImportantQuestions
from conftest import driver


class TestImportantQuestions:
        @allure.title('Проверка клика по строке Сколько это стоит')
        def test_click_how_much_does_it_cost(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_how_much_does_it_cost()
            assert important_questions.find_element(ImportantQuestionsLocators.how_much_does_it_cost_is_open)

        @allure.title('Проверяем клик по строке Хочу сразу несколько самокатов')
        def test_click_i_want_some_scooters(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_i_want_some_scooters()
            assert important_questions.find_element(ImportantQuestionsLocators.i_want_some_scooters_is_open)

        @allure.title('Проверяем клик по строке Как рассчитывается время аренды?')
        def test_click_how_is_the_rental_time_calculated(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_how_is_the_rental_time_calculated()
            assert important_questions.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open)

        @allure.title('Проверяем клик по строке Можно ли заказать самокат прямо на сегодня?')
        def test_click_can_i_order_a_scooter_for_today(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_can_i_order_a_scooter_for_today()
            assert important_questions.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open)

        @allure.title('Проверяем клик по строке Можно ли продлить заказ или вернуть самокат раньше?')
        def tets_click_is_it_possible_to_extend_the_order(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_is_it_possible_to_extend_the_order()
            assert important_questions.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

        @allure.title('Проверяем клик по строке Вы привозите зарядку вместе с самокатом?')
        def test_click_do_you_bring_charger(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_do_you_bring_charger()
            assert important_questions.find_element(ImportantQuestionsLocators.do_you_bring_charger_is_open)

        @allure.title('Проверяем клик по строке Можно ли отменить заказ?')
        def test_click_is_it_possible_to_cancel_an_order(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_is_it_possible_to_cancel_an_order()
            assert important_questions.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

        @allure.title('Проверяем клик по строке Я жизу за МКАДом, привезёте?')
        def test_click_i_live_beyond_the_mkad(self, driver):
            important_questions = ImportantQuestions(driver)
            important_questions.go_to_site()
            important_questions.click_i_live_beyond_the_mkad()
            assert important_questions.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open)


