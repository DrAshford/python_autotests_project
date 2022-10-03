from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_cost = page.get_product_cost()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    added_product = page.get_added_product()
    basket_total = page.get_basket_total()
    assert product_name == added_product, f'Adding error: expected add "{product_name}" not "{added_product}"!'
    assert product_cost == basket_total, f'Adding error: expected basket total: {product_cost} not: {basket_total}!' 