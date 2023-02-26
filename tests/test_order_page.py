import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestOrder():

    @allure.title('Успешное оформление заказа')
    def test_order(self, order_page):
        for user in OrderPage.USERS:
            order_page.find_element(OrderPage.input_name).send_keys(user.get('Имя'))
            order_page.find_element(OrderPage.input_surname).send_keys(user.get('Фамилия'))
            order_page.find_element(OrderPage.input_address).send_keys(user.get('Адрес'))
            order_page.find_element(OrderPage.input_metro).send_keys(user.get('Метро'))
            order_page.click_element(OrderPage.select_metro)
            order_page.find_element(OrderPage.input_phone).send_keys(user.get('Телефон'))
            order_page.click_element(OrderPage.next_button)
            d = order_page.find_element(OrderPage.input_date)
            d.send_keys(user.get('Дата'))
            d.send_keys(Keys.ESCAPE)
            order_page.click_element(OrderPage.due_date)
            order_page.click_element(OrderPage.due_date_variants)
            order_page.click_element(OrderPage.order_button_form)
            order_page.click_element(OrderPage.yes_button)
            assert "Заказ оформлен" in order_page.element_text(OrderPage.order_done)
            order_page.go_to_order_page()


    @allure.title('Проверка перехода на главную страницу при нажатии на лого "Самокат"')
    def test_click_logo_scooter(self, order_page):
        order_page.click_element(BasePage.logo_scooter)
        assert order_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на главную страницу Яндекса при нажатии на лого "Яндекс"')
    def test_click_logo_ya(self, order_page):
        original_window = order_page.driver.current_window_handle
        order_page.click_element(BasePage.logo_yandex)
        WebDriverWait(order_page.driver, 10).until(EC.number_of_windows_to_be(2))
        order_page.driver.switch_to.window([x for x in order_page.driver.window_handles if x not in original_window][0])
        WebDriverWait(order_page.driver, 10).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert order_page.driver.current_url == 'https://dzen.ru/?yredirect=true'



