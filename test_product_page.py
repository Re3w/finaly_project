import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.locators import LoginPageLocators, BasePageLocators


@pytest.mark.need_review
# @pytest.mark.parametrize('links', [i if i != 7 else pytest.param(i, marks=pytest.mark.xfail) for i in range(10)])
@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                                "/?promo=offer7", marks=pytest.mark.xfail),
                                   #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = links  # f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    # "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_promo_product()
    page.check_price_adding_to_cart()
    page.check_mess_adding_to_cart()
    page.should_be_success_message()
    page.should_not_be_success_message()
    page.should_see_as_disappearing_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_promo_product()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_promo_product()
    page.should_see_as_disappearing_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_open_can_go_to_basket_page()
    page.should_be_the_message_cart_is_empty()
    page.checking_no_items_in_cart()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.is_not_element_present(*LoginPageLocators.REGISTER_FORM)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.is_not_element_present(*BasePageLocators.USER_ICON)
        self.page.should_be_authorized_user()

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_promo_product()
        page.check_price_adding_to_cart()
        page.check_mess_adding_to_cart()
        page.should_be_success_message()
        page.should_not_be_success_message()
        page.should_see_as_disappearing_message()
