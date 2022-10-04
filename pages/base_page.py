from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocator
import math
import time


class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #Возвращает указатель на элемент, если он есть на странице 
    def get_element(self, how, what):
        if self.is_element_present(how, what):
            element = self.browser.find_element(how, what)
            element.location_once_scrolled_into_view
            return element
        print("Element is not presented!")
        return None

    def is_not_element_present(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocator.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocator.LOGIN_LINK), 'Login link is not presented'

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocator.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocator.USER_ICON), 'User icon is not presented, probably unauthorized user'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            #time.sleep(3000)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    