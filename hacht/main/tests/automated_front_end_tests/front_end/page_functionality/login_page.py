
from ..Base import Base
class Login_page(Base):

    def __init__(self, driver):

        self.form_login_email = '//*[@id="email"]'
        self.form_login_password = '//*[@id="password"]'
        self.form_login_submit = '/html/body/main/section/div/form/button'
        self.login_failed_text = '/html/body/main/section/div/form/p'
        self.mantener_sesion = '//*[@id="checkbox"]'

        super(Login_page, self).__init__(driver)


    def iniciar_sesion(self, email, password, mantener_sesion):
        self.x_write_entry(email, self.form_login_email)
        self.x_write_entry(password, self.form_login_password)
        if(mantener_sesion): self.x_click(self.mantener_sesion)

        self.x_click(self.form_login_submit)
