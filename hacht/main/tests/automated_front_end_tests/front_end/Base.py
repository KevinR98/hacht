from django.test import TestCase
from selenium import webdriver

class Base:

    def __init__(self, webdriver):
        self.driver = webdriver

    def firefox_webdriver(self):
        return webdriver.Firefox()

    def go_to(self, locator):
        self.driver.get(locator)

    def x_click(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()

    def get_url(self):
        url = self.driver.current_url
        return url

