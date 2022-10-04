from selenium.webdriver.common.by import By

class BasePageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME  = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alert-info strong')
    MESSAGE_ADDED_PRODUCT = (By.CSS_SELECTOR, 'div#messages :nth-child(1) strong')

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-1 p.price_color')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '.content p')