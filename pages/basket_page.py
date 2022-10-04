from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Basket is not empty but should be!'

    def should_be_text_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), 'Message about empty basket is not present!'    
