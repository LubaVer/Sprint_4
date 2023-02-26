import allure

from pages.main_page import MainPage


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

    @allure.title('Переход на страницу заказа через кнопку вверху страницы')
    def test_open_order_page_with_middle_button(self, main_page):
        main_page.scroll_to_element(MainPage.order_button_middle)
        main_page.click_element(MainPage.order_button_middle)
        assert main_page.current_url() == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Переход на страницу заказа через кнопку вверху страницы')
    def test_open_order_page_with_heder_button(self, main_page):
        main_page.click_element(MainPage.order_button)
        assert main_page.current_url() == 'https://qa-scooter.praktikum-services.ru/order'