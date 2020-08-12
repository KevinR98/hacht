
from selenium import webdriver
from ..Base import Base
from .index_page import Index_page

class Login_page(Base):

    def __init__(self, driver):

        self.form_login_email = '//*[@id="email"]'
        self.form_login_password = '//*[@id="password"]'
        self.form_login_submit = '/html/body/main/section/div/form/button'
        self.login_failed_text = '/html/body/main/section/div/form/p'

        super(Login_page, self).__init__(driver)


    def iniciar_sesion(self, email, password):
        self.x_write_entry(email, self.form_login_email)
        self.x_write_entry(email, self.form_login_password)

        self.x_click(self.form_login_submit)

        return Index_page(self.driver)