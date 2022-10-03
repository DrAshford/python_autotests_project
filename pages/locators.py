from selenium.webdriver.common.by import By

class BasePageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME  = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alert-info strong')
    MESSAGE_ADDED_PRODUCT = (By.CSS_SELECTOR, 'div#messages :nth-child(1) strong')