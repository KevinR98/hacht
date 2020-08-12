
from selenium import webdriver
from ..Base import Base

class Help_page(Base):

    def __init__(self):

        super(Help_page, self).__init__(Base.firefox_webdriver(self))
        self.driver.get('http://127.0.0.1:8000/')



