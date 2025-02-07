from selenium.webdriver.common.by import By
class ImportantQuestionsLocators:
    how_much_does_it_cost = [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div']
    how_much_does_it_cost_is_open = (By.XPATH, '//div[@id="accordion__panel-0"]')
    i_want_some_scooters = [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div']
    i_want_some_scooters_is_open = (By.XPATH, '//div[@id="accordion__panel-1"]')
    how_is_the_rental_time_calculated = [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div']
    how_is_the_rental_time_calculated_is_open = (By.XPATH, '//div[@id="accordion__panel-2"]')
    can_i_order_a_scooter_for_today = [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div']
    can_i_order_a_scooter_for_today_is_open = (By.XPATH, '//div[@id="accordion__panel-3"]')
    is_it_possible_to_extend_the_order = [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div']
    is_it_possible_to_extend_the_order_is_open = (By.XPATH, '//div[@id="accordion__panel-4"]')
    do_you_bring_charger = [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div']
    do_you_bring_charger_is_open = (By.XPATH, '//div[@id="accordion__panel-5"]')
    is_it_possible_to_cancel_an_order = [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div']
    is_it_possible_to_cancel_an_order_is_open = (By.XPATH, '//div[@id="accordion__panel-6"]')
    i_live_beyond_the_MKAD = [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    i_live_beyond_the_MKAD_is_open = (By.XPATH, '//div[@id="accordion__panel-7"]')

class OrderPageLocators:
    the_order_button_at_the_top_of_the_page = [By.XPATH,"//button[@class='Button_Button__ra12g']"]
    the_order_button_at_the_bottom_of_the_page = [By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    name_input_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_input_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input_field = [By.XPATH,"//input[@class ='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ']"]
    metro_station = [By.XPATH, "//input[@class ='select-search__input']"]
    phone_input_field = [By.XPATH, "//input[@class ='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Телефон: на него позвонит курьер']"]
    the_next_button = [By.XPATH, "//button[@class ='Button_Button__ra12g Button_Middle__1CSJM']"]
    when_to_bring_the_scooter = [By.XPATH, "//input[@class ='Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside' and @placeholder='* Когда привезти самокат']"]
    rental_period = [By.XPATH, "//div[@class ='Dropdown-placeholder']"]
    scooter_color = [By.XPATH, "//div[@class ='Order_Title__3EKne']"]
    comment_for_the_courier = [By.XPATH, "//input[@class ='Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside' and @placeholder='Комментарий для курьера']"]
    the_order_button_in_the_order_form = [By.XPATH, "//button[@class ='Button_Button__ra12g Button_Middle__1CSJM']"]
    yes_button = [By.XPATH, "//button[@class='Button_Buttonra12g Button_Middle1CSJM' and text()='Да']"]
    order_registration = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    checkbox_blak = [By.ID, 'black']
    checkbox_grey = [By.ID, 'grey']
    view_the_status = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    scooter_logo = [By.XPATH, "//img[@src='/assets/scooter.svg']"]
    yandex_logo = [By.XPATH,"//img[@src='/assets/ya.svg']"]
    metro_sokolniki = [By.XPATH, "//div[text()='Сокольники']"]
    dvoe_sutok  = [By.XPATH, ".//*[text() = 'Двое суток']"]
    metro_lubyanka = [By.XPATH, "//div[text()='Лубянка']"]
    troe_sutok  = [By.XPATH, ".//*[text() = 'Трое суток']"]