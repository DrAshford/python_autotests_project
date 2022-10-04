from email.mime import base

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from python_autotests_project.pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
import pytest
import faker


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
  page = ProductPage(browser, link)
  page.open()
  page.add_product_to_basket()
  page.solve_quiz_and_get_code()
  page.should_be_added_product_name()
  page.should_be_added_product_cost()

  

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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
  page = ProductPage(browser, link)
  page.open()
  page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  page = ProductPage(browser, link)
  page.open()
  page.go_to_basket_page()
  basket_page = BasketPage(browser, browser.current_url)
  basket_page.should_be_empty()
  basket_page.should_be_text_about_basket_empty()

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
  @pytest.fixture(scope="function", autouse=True)
  def setup(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    email_gen = faker.Faker()
    email = email_gen.email()
    password = '!19B24RLO@#'
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()

  def test_user_cant_see_success_message(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

  @pytest.mark.need_review
  def test_user_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_product_name()
    page.should_be_added_product_cost()