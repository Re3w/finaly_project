from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_the_message_cart_is_empty(self):
        mess = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
        assert not self.is_not_element_present(
            *BasketPageLocators.MESSAGE_EMPTY_BASKET) and "Your basket is empty." in mess.text, "No empty cart message"

    def checking_no_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_ITEMS), "There are items in the cart"