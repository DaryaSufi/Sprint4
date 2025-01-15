import allure
import pytest

from locators import ImportantQuestionsLocators
from pages.important_questions_page import ImportantQuestions
from conftest import driver


class TestImportantQuestions:

    @pytest.mark.parametrize('expected_element',[ImportantQuestionsLocators.how_much_it_does_cost_is_open,
                                                 ImportantQuestionsLocators.i_want_some_scooter_is_open,
                                                 ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open,
                                                 ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open,
                                                 ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open,
                                                 ImportantQuestionsLocators.do_you_bring_charger_is_open,
                                                 ImportantQuestionsLocators.is_it_possible_to_cancel_an_order_is_open,
                                                 ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open])
    def test_click_important_questions_line(self,expected_elements):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_important_questions_line
        assert driver.find_element(expected_elements)

    @allure.title
    def test_click_how_much_does_it_cost(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_how_much_does_it_cost
        assert important_questions.find_element(ImportantQuestionsLocators.how_much_does_it_cost_is_open)

    @allure.title
    def test_click_i_want_some_scooters(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_i_want_some_scooters
        assert driver.find_element(ImportantQuestionsLocators.i_want_some_scooters_is_open)

    @allure.title
    def test_click_how_is_the_rental_time_calculated(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_how_is_the_rental_time_calculated
        assert driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open)

    @allure.title
    def test_click_can_i_order_a_scooter_for_today(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_can_i_order_a_scooter_for_today
        assert driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open)

    @allure.title
    def tets_click_is_it_possible_to_extend_the_order(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_is_it_possible_to_extend_the_order
        assert driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

    @allure.title
    def test_click_do_you_bring_charger(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_do_you_bring_charger
        assert driver.find_element(ImportantQuestionsLocators.do_you_bring_charger_is_open)

    @allure.title
    def test_click_is_it_possible_to_cancel_an_order(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_is_it_possible_to_cancel_an_order
        assert driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

    @allure.title
    def test_click_i_live_beyond_the_mkad(self, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        important_questions.click_i_live_beyond_the_mkad
        assert driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open)

