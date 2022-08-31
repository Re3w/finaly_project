from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div #login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div #register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_ADDING = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRICE_PRODUCT_MAIN = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_MAIN_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_PRODUCT_FROM_ALERT = (By.CSS_SELECTOR, "div#messages :first-child :nth-child(2) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner")

