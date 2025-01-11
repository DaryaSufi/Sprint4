import allure

from locators import ImportantQuestionsLocators


class TestImportantQuestions:

    @allure.step
    def test_click_how_much_does_it_cost(self, driver):
        driver.find_element(ImportantQuestionsLocators.how_much_does_it_cost).click()
        assert driver.find_element(ImportantQuestionsLocators.how_much_does_it_cost_is_open)

    @allure.step
    def test_click_i_want_some_scooters(self, driver):
        driver.find_element(ImportantQuestionsLocators.i_want_some_scooters).click()
        assert driver.find_element(ImportantQuestionsLocators.i_want_some_scooters_is_open)

    @allure.step
    def test_click_how_is_the_rental_time_calculated(self, driver):
        driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated).click()
        assert driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open)

    @allure.step
    def test_click_can_i_order_a_scooter_for_today(self, driver):
        driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today).click()
        assert driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open)

    @allure.step
    def tets_click_is_it_possible_to_extend_the_order(self, driver):
        driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order).click()
        assert driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

    @allure.step
    def test_click_do_you_bring_charger(self, driver):
        driver.find_element(ImportantQuestionsLocators.do_you_bring_charger).click()
        assert driver.find_element(ImportantQuestionsLocators.do_you_bring_charger_is_open)

    @allure.step
    def test_click_is_it_possible_to_cancel_an_order(self, driver):
        driver.find_element(ImportantQuestionsLocators.is_it_possible_to_cancel_an_order).click()
        assert driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open)

    @allure.step
    def test_click_i_live_beyond_the_mkad(self, driver):
        driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD).click()
        assert driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open)

