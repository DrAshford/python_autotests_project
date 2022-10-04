from email.mime import base
from .pages.basket_page import BasketPage
from python_autotests_project.pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

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

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  page = ProductPage(browser, link)
  page.open()
  page.add_product_to_basket()
  page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
  page = ProductPage(browser, link)
  page.open()
  page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
  page = ProductPage(browser, link)
  page.open()
  page.add_product_to_basket()
  page.should_be_disappeared_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
  page = ProductPage(browser, link)
  page.open()
  page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
  page = ProductPage(browser, link)
  page.open()
  page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  page = ProductPage(browser, link)
  page.open()
  page.go_to_basket_page()
  basket_page = BasketPage(browser, browser.current_url)
  basket_page.should_be_empty()
  basket_page.should_be_text_about_basket_empty()