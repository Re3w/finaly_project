from .base_page import BasePage, MathPromo
from .locators import ProductPageLocators


class ProductPage(BasePage, MathPromo, ProductPageLocators):
    def add_to_basket_promo_product(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_to_cart.click()
        self.solve_quiz_and_get_code()

    def check_price_adding_to_cart(self):
        pm = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MAIN)#(self.PRICE_PRODUCT_MAIN[0], self.PRICE_PRODUCT_MAIN[1]).text
        pfa = self.browser.find_element(*ProductPageLocators.PRICE_ADDING)#(self.PRICE_ADDING[0], self.PRICE_ADDING[1]).text
        assert pm.text == pfa.text, "Error in the price of the added product"

    def check_mess_adding_to_cart(self):
        np = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_MAIN_ON_PAGE)#(self.NAME_PRODUCT_MAIN_ON_PAGE[0], self.NAME_PRODUCT_MAIN_ON_PAGE[1]).text
        npf = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_FROM_ALERT)#(self.NAME_PRODUCT_FROM_ALERT[0], self.NAME_PRODUCT_FROM_ALERT[1]).text
        assert np.text == npf.text, "Error in the name of the added product"
