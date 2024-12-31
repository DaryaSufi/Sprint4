from locators import ImportantQuestionsLocators

class ImportantQuestions:

    how_much_does_it_cost = ImportantQuestionsLocators.how_much_does_it_cost
    how_much_does_it_cost_is_open = ImportantQuestionsLocators.how_much_does_it_cost_is_open
    i_want_some_scooters = ImportantQuestionsLocators.i_want_some_scooters
    i_want_some_scooters_is_open = ImportantQuestionsLocators.how_much_does_it_cost_is_open
    how_is_the_rental_time_calculated = ImportantQuestionsLocators.how_is_the_rental_time_calculated
    how_is_the_rental_time_calculated_is_open = ImportantQuestionsLocators.how_is_the_rental_time_calculated_is_open
    can_i_order_a_scooter_for_today = ImportantQuestionsLocators.can_i_order_a_scooter_for_today
    can_i_order_a_scooter_for_today_is_open = ImportantQuestionsLocators.can_i_order_a_scooter_for_today_is_open
    is_it_possible_to_extend_the_order = ImportantQuestionsLocators.is_it_possible_to_extend_the_order
    is_it_possible_to_extend_the_order_is_open = ImportantQuestionsLocators.is_it_possible_to_extend_the_order_is_open
    do_you_bring_charger = ImportantQuestionsLocators.do_you_bring_charger
    do_you_bring_charger_is_open = ImportantQuestionsLocators.do_you_bring_charger_is_open
    is_it_possible_to_cancel_an_order = ImportantQuestionsLocators.is_it_possible_to_cancel_an_order
    is_it_possible_to_cancel_an_order_is_open = ImportantQuestionsLocators.is_it_possible_to_cancel_an_order_is_open
    i_live_beyond_the_MKAD = ImportantQuestionsLocators.i_live_beyond_the_MKAD
    i_live_beyond_the_MKAD_is_open = ImportantQuestionsLocators.i_live_beyond_the_MKAD_is_open

    def __init__(self,driver):
        self.driver=driver

    def click_how_much_does_it_cost(self):
        self.driver.find_element(ImportantQuestionsLocators.how_much_does_it_cost).click()

    def click_i_want_some_scooters(self):
        self.driver.find_element(ImportantQuestionsLocators.i_want_some_scooters).click()

    def click_how_is_the_rental_time_calculated(self):
        self.driver.find_element(ImportantQuestionsLocators.how_is_the_rental_time_calculated).click()

    def click_can_i_order_a_scooter_for_today(self):
        self.driver.find_element(ImportantQuestionsLocators.can_i_order_a_scooter_for_today).click()

    def click_is_it_possible_to_extend_the_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_extend_the_order).click()

    def click_do_you_bring_charger(self):
        self.driver.find_element(ImportantQuestionsLocators.do_you_bring_charger).click()

    def click_is_it_possible_to_cancel_an_order(self):
        self.driver.find_element(ImportantQuestionsLocators.is_it_possible_to_cancel_an_order).click()

    def click_i_live_beyond_the_mkad(self):
        self.driver.find_element(ImportantQuestionsLocators.i_live_beyond_the_MKAD).click()
