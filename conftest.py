import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def browser():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1200,800)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(browser):
    mp = MainPage(browser)
    mp.go_to_site()
    return mp

@pytest.fixture
def order_page(browser):
    page = OrderPage(browser)
    page.go_to_order_page()
    return page