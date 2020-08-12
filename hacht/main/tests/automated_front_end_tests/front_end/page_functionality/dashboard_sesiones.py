
from selenium import webdriver
from ..Base import Base

class Dashboard_sesiones_page(Base):

    def __init__(self):

        super(Dashboard_sesiones_page, self).__init__(Base.firefox_webdriver(self))
        self.driver.get('http://127.0.0.1:8000/')


