import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.common.keys import Keys


class TestQuestions():

    @allure.title('Проверка корректности названия FAQ')
    def test_questions_about_important(self, main_page):
        main_page.scroll_faq()
        assert main_page.element_text(MainPage.important_header) == 'Вопросы о важном'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Сколько это стоит? И как оплатить?"')
    def test_faq_cost(self, main_page):
        main_page.scroll_to_element(MainPage.how_cost_heading)
        main_page.click_element(MainPage.how_cost_heading)
        assert main_page.element_text(MainPage.how_cost_text) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Хочу сразу несколько самокатов! Так можно?"')
    def test_faq_several_scooters(self, main_page):
        main_page.scroll_to_element(MainPage.several_scooters_heading)
        main_page.click_element(MainPage.several_scooters_heading)
        assert main_page.element_text(MainPage.several_scooters_text) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Как рассчитывается время аренды?"')
    def test_faq_rental_time(self, main_page):
        main_page.scroll_to_element(MainPage.rental_time_heading)
        main_page.click_element(MainPage.rental_time_heading)
        assert main_page.element_text(MainPage.rental_time_text) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Можно ли заказать самокат прямо на сегодня?"')
    def test_faq_order_today(self, main_page):
        main_page.scroll_to_element(MainPage.order_today_heading)
        main_page.click_element(MainPage.order_today_heading)
        assert main_page.element_text(
            MainPage.order_today_text) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_faq_extend_order(self, main_page):
        main_page.scroll_to_element(MainPage.extend_order_heading)
        main_page.click_element(MainPage.extend_order_heading)
        assert main_page.element_text(
            MainPage.extend_order_text) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Вы привозите зарядку вместе с самокатом?"')
    def test_faq_charging(self, main_page):
        main_page.scroll_to_element(MainPage.charging_heading)
        main_page.click_element(MainPage.charging_heading)
        assert main_page.element_text(
            MainPage.charging_text) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Можно ли отменить заказ?"')
    def test_faq_cancel_order(self, main_page):
        main_page.scroll_to_element(MainPage.cancel_order_heading)
        main_page.click_element(MainPage.cancel_order_heading)
        assert main_page.element_text(
            MainPage.cancel_order_text) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка ответов выпадающего списка FAQ. "Я живу за МКАДом, привезёте?"')
    def test_faq_live_outside_mkad(self, main_page):
        main_page.scroll_to_element(MainPage.live_outside_mkad_heading)
        main_page.click_element(MainPage.live_outside_mkad_heading)
        assert main_page.element_text(
            MainPage.live_outside_mkad_text) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class TestOpenOrderPage():


    @allure.title('Переход на страницу заказа через кнопку внизу страницы')
    def test_open_order_page_with_middle_button(self, main_page):
        main_page.scroll_to_element(MainPage.order_button_middle)
        main_page.click_element(MainPage.order_button_middle)
        assert main_page.current_url() == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Переход на страницу заказа через кнопку вверху страницы')
    def test_open_order_page_with_heder_button(self, main_page):
        main_page.click_element(MainPage.order_button)
        assert main_page.current_url() == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Успешное оформление заказа через кнопку вверху страницы')
    @pytest.mark.parametrize('user', OrderPage.USERS)
    def test_order_with_heder_button(self, main_page, user):
        main_page.click_element(MainPage.order_button)
        main_page.find_element(OrderPage.input_name).send_keys(user.get('Имя'))
        main_page.find_element(OrderPage.input_surname).send_keys(user.get('Фамилия'))
        main_page.find_element(OrderPage.input_address).send_keys(user.get('Адрес'))
        main_page.find_element(OrderPage.input_metro).send_keys(user.get('Метро'))
        main_page.click_element(OrderPage.select_metro)
        main_page.find_element(OrderPage.input_phone).send_keys(user.get('Телефон'))
        main_page.click_element(OrderPage.next_button)
        d = main_page.find_element(OrderPage.input_date)
        d.send_keys(user.get('Дата'))
        d.send_keys(Keys.ESCAPE)
        main_page.click_element(OrderPage.due_date)
        main_page.click_element(OrderPage.due_date_variants)
        main_page.click_element(OrderPage.order_button_form)
        main_page.click_element(OrderPage.yes_button)
        assert "Заказ оформлен" in main_page.element_text(OrderPage.order_done)

    @allure.title('Успешное оформление заказа через кнопку внизу страницы')
    @pytest.mark.parametrize('user', OrderPage.USERS)
    def test_order(self, main_page, user):
        main_page.scroll_to_element(MainPage.order_button_middle)
        main_page.click_element(MainPage.order_button_middle)
        main_page.find_element(OrderPage.input_name).send_keys(user.get('Имя'))
        main_page.find_element(OrderPage.input_surname).send_keys(user.get('Фамилия'))
        main_page.find_element(OrderPage.input_address).send_keys(user.get('Адрес'))
        main_page.find_element(OrderPage.input_metro).send_keys(user.get('Метро'))
        main_page.click_element(OrderPage.select_metro)
        main_page.find_element(OrderPage.input_phone).send_keys(user.get('Телефон'))
        main_page.click_element(OrderPage.next_button)
        d = main_page.find_element(OrderPage.input_date)
        d.send_keys(user.get('Дата'))
        d.send_keys(Keys.ESCAPE)
        main_page.click_element(OrderPage.due_date)
        main_page.click_element(OrderPage.due_date_variants)
        main_page.click_element(OrderPage.order_button_form)
        main_page.click_element(OrderPage.yes_button)
        assert "Заказ оформлен" in main_page.element_text(OrderPage.order_done)