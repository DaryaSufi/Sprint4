import allure
import pytest
from pages.important_questions_page import ImportantQuestions


class TestImportantQuestions():
    @allure.title("Проверка открытия важных вопросов")
    @pytest.mark.parametrize('function_name, expected_element', [
        ('click_how_much_does_it_cost', 'ImportantQuestionsLocators.how_much_does_it_cost_is_open'),
        ('click_i_want_some_scooters', 'ImportantQuestionsLocators.i_want_some_scooters_is_open'),
        ('click_how_is_the_rental_time_calculated',
         'ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open'),
        ('click_can_i_order_a_scooter_for_today',
         'ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open'),
        ('click_is_it_possible_to_extend_the_order',
         'ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open'),
        ('click_do_you_bring_charger', 'ImportantQuestionsLocators.do_you_bring_charger_is_open'),
        ('click_is_it_possible_to_cancel_an_order',
         'ImportantQuestionsLocators.is_it_possible_to_cancel_an_order_is_open'),
        ('click_i_live_beyond_the_MKAD', 'ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open')
    ])
    def test_important_questions(self, function_name, expected_element, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.go_to_site()
        getattr(important_questions, function_name)()
        assert important_questions.find_element(expected_element)


