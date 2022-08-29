import time
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

def test_search_button_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()