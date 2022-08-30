from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage, MainPageLocators):
    def go_to_login_page(self):
        login_link = self.browser.find_element(self.LOGIN_LINK[0], self.LOGIN_LINK[1])
        login_link.click()
#        alert = self.browser.switch_to.alert
#        alert.accept()
        #return LoginPage(browser=self.browser, url=self.check_url())

    def should_be_login_link(self):
        assert not self.is_element_present(self.LOGIN_LINK[0], self.LOGIN_LINK[1] + "_invalid"), "Login link is not presented"
