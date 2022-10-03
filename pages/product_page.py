from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    #Добавить товар в корзину
    def add_product_to_basket(self):
        button = self.get_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    #Проверить наличие цены товара
    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), 'Product cost is not presented'

    #Получить цену товара
    def get_product_cost(self):
        self.should_be_product_cost()
        return self.get_element(*ProductPageLocators.PRODUCT_COST).text

    #Проверить наличие названия товара
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name is not presented'

    #Получить название товара
    def get_product_name(self):
        self.should_be_product_name()
        return self.get_element(*ProductPageLocators.PRODUCT_NAME).text
    
    #Проверить наличие сообщения о добавленном товаре
    def should_be_added_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_PRODUCT), 'Added product is not presented'

    #Получить название добавленного товара
    def get_added_product(self):
        self.should_be_added_product()
        return self.get_element(*ProductPageLocators.MESSAGE_ADDED_PRODUCT).text

    #Проверить наличие суммы корзины
    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), 'Basket total is not presented'

    def get_basket_total(self):
        self.should_be_basket_total()
        return self.get_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_PRODUCT), \
        'Success message is presented, but should not be'

    def should_be_disappeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_PRODUCT), \
        'Message not disappeared but should be'