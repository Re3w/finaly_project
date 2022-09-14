from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_SUMMARY_ITEMS = (By.CSS_SELECTOR, "form.basket_summary")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div #login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div #register_form")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASS_INPUT_1 = (By.ID, "id_registration-password1")
    PASS_INPUT_2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_ADDING = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRICE_PRODUCT_MAIN = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_MAIN_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_PRODUCT_FROM_ALERT = (By.CSS_SELECTOR, "div#messages :first-child :nth-child(2) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner")
