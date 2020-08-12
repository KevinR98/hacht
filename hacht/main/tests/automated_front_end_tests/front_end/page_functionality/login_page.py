
from selenium import webdriver
from ..Base import Base

class Login_page(Base):

    def __init__(self, driver):

        self.form_login_email = '//*[@id="email"]'
        self.form_login_password = '//*[@id="password"]'
        self.form_login_submit = '/html/body/main/section/div/form/button'

        super(Login_page, self).__init__(driver)


    def iniciar_sesion(self, email, password):
        self.x_write_entry(email, self.form_login_email)
        self.x_write_entry(email, self.form_login_password)

        self.x_click(self.form_login_submit)