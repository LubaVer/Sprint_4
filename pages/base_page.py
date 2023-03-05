import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    order_button = [By.XPATH, "//button[@class ='Button_Button__ra12g']"]
    logo_yandex = [By.XPATH, "//a[@class ='Header_LogoYandex__3TSOI']"]
    logo_scooter = [By.XPATH, "//a[@class ='Header_LogoScooter__3lsAR']"]
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открываем сайт')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Открываем страницу сайта')
    def go_to_page(self, page):
        return self.driver.get(self.base_url+page)


    @allure.step('Ищем элемент')
    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f"Not found {locator}")

    @allure.step('Ищем элементы')
    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Not found {locator}")

    @allure.step('Получаем текст элемента')
    def element_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Скроллим')
    def scroll_to_element(self, locator, time = 10):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                               message=f"Not found {locator}")

    @allure.step('Нажимаем на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Получаем текущий адрес браузера')
    def current_url(self):
        return self.driver.current_url


