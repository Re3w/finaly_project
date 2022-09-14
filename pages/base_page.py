import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators


class MathPromo:  # РЕШЕНИЕ КАПЧИ ДЛЯ РОБОТОВ
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def check_url(self):  # ПРОВЕРКА УРЛЫ НА ВАЛИДНОСТЬ
        return self.browser.current_url

    def check_message_of_empty_basket(self):
        mess = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
        assert "Your basket is empty." not in mess.text, "Your basket in not empty"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def guest_open_can_go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button.click()

    def is_disappeared(self, how, what, timeout=4):  # ПРОВЕРКА НА ЗАКРЫТИЕ ЭЛЕМЕНТА
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how,
                                                                                                                what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # ПРИСУТСТВИЕ ЭЛЕМЕНТА НА СТРАНИЦЕ
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):  # ОТКРЫТИЕ ССЫЛКИ
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.check_url(), "Invalid link address"


"""
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

Args:

driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
timeout - Number of seconds before timing out
poll_frequency - sleep interval between calls By default, it is 0.5 second.
ignored_exceptions - iterable structure of exception classes ignored during calls. By default, it contains NoSuchElementException only.
"""
