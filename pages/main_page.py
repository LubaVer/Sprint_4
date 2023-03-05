import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    important_header = [By.XPATH, "//div[contains(text(),'Вопросы о важном')]"]

    how_cost_heading = [By.ID, "accordion__heading-0"]
    how_cost_text = [By.ID, "accordion__panel-0"]
    several_scooters_heading = [By.ID, "accordion__heading-1"]
    several_scooters_text = [By.ID, "accordion__panel-1"]
    rental_time_heading = [By.ID, "accordion__heading-2"]
    rental_time_text = [By.ID, "accordion__panel-2"]
    order_today_heading = [By.ID, "accordion__heading-3"]
    order_today_text = [By.ID, "accordion__panel-3"]
    extend_order_heading = [By.ID, "accordion__heading-4"]
    extend_order_text = [By.ID, "accordion__panel-4"]
    charging_heading = [By.ID, "accordion__heading-5"]
    charging_text = [By.ID, "accordion__panel-5"]
    cancel_order_heading = [By.ID, "accordion__heading-6"]
    cancel_order_text = [By.ID, "accordion__panel-6"]
    live_outside_mkad_heading = [By.ID, "accordion__heading-7"]
    live_outside_mkad_text = [By.ID, "accordion__panel-7"]

    order_button_middle = [By.XPATH, "//button[@class ='Button_Button__ra12g Button_Middle__1CSJM']"]

    @allure.step('Скроллим до "Вопросы о важном"')
    def scroll_faq(self):
        self.scroll_to_element(self.important_header)
