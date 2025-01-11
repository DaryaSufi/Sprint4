import allure

from locators import ImportantQuestionsLocators


class ImportantQuestions:
    def __init__(self,driver):
        self.driver=driver

    @allure.step
    def click_how_much_does_it_cost(self):
        self.driver.find_element(ImportantQuestionsLocators.how_much_does_it_cost).click()

    @allure.step
    def click_i_want_some_scooters(self):
        self.driver.find_element(ImportantQuestionsLocators.i_want_some_scooters).click()

    @allure.step
    def click_how_is_the_rental_time_calculated(self):
        self.driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated).click()

    @allure.step
    def click_can_i_order_a_scooter_for_today(self):
        self.driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today).click()

    @allure.step
    def click_is_it_possible_to_extend_the_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order).click()

    @allure.step
    def click_do_you_bring_charger(self):
        self.driver.find_element(ImportantQuestionsLocators.do_you_bring_charger).click()

    @allure.step
    def click_is_it_possible_to_cancel_an_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_cancel_an_order).click()

    @allure.step
    def click_i_live_beyond_the_mkad(self):
        self.driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD).click()
