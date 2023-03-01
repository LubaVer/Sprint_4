from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):

    USERS = [
        {
            "Имя": "Иван",
            "Фамилия": "Иванов",
            "Адрес": "ул. Доватора, 10",
            "Метро": "Спортивная",
            "Телефон": "89991234567",
            "Дата": "12.12.2023",

        },
        {
            "Имя": "Ян",
            "Фамилия": "Ли",
            "Адрес": "Варшавское ш., 80",
            "Метро": "Варшавская",
            "Телефон": "89991234567",
            "Дата": "12.05.2023",
        }
    ]

    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    select_metro = [By.CLASS_NAME, "select-search__row"]
    input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    input_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    next_button = [By.XPATH, "//button[contains(text(),'Далее')]"]
    due_date = [By.XPATH,"//div[contains(text(),'* Срок аренды')]"]
    due_date_variants = [By.XPATH, "//div[@class='Dropdown-option']"]
    order_button_form = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    yes_button = [By.XPATH, "//button[contains(text(),'Да')]"]
    order_done = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    back_button = [By.XPATH, "//button[contains(text(),'Назад')]"]
    header_for_who = [By.XPATH, "//div[contains(text(),'Для кого самокат')]"]
    header_about_borrow = [By.XPATH, "//div[contains(text(),'Про аренду')]"]
    def go_to_order_page(self):
        self.go_to_page('order')
