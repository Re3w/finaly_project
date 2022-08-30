from .pages.product_page import ProductPage


def test_add_to_basket_promo_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_promo_product()
    page.check_price_adding_to_cart()
    page.check_mess_adding_to_cart()
