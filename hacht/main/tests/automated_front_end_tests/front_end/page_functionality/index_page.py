
from .contact_us_page import Contact_us_page
from .dashboard_pacientes import Dashboard_pacientes_page
from .dashboard_sesiones import Dashboard_sesiones_page
from .demo_page import Demo_page
from .features_page import Features_page
from .help_page import Help_page
from .about_us_page import About_us_page
from .login_page import Login_page
from .registration_page import Registration_page

from ..Base import Base

class Index_page(Base):

    def __init__(self, driver):
        self.hacht_logo = '/html/body/nav/div/a'
        self.user_email_text = '/html/body/nav/div/span'

        self.header_inicio = '/html/body/nav/div/div/ul/li[6]/a'
        self.header_demo = '/html/body/nav/div/div/ul/li[2]/a'
        self.header_caracteristicas = '/html/body/nav/div/div/ul/li[3]/a'
        self.header_sobre_nosotros = '/html/body/nav/div/div/ul/li[4]/a'
        self.header_contactenos = '/html/body/nav/div/div/ul/li[3]/a'
        self.header_resgistrarse = '/html/body/nav/div/div/ul/li[5]/a'
        self.header_ingresar = '/html/body/nav/div/div/ul/li[6]/a'
        self.header_ayuda = '/html/body/nav/div/div/ul/li[1]/a/span'

        self.log_header_mis_pacientes = '/html/body/nav/div/div/ul/li[1]/a/span'
        self.log_header_cerrar = '/html/body/nav/div/div/ul/li[6]/a/span'
        self.log_header_mis_sesiones = '/html/body/nav/div/div/ul/li[1]/a/span'


        self.footer_ayuda = '/html/body/footer/div[1]/div/div[3]/ul/li[1]/a'

        super(Index_page, self).__init__(driver)



    def click_header_demo(self):
        self.x_click(self.header_demo)
        return Demo_page(self.driver)

    def click_header_caracteristicas(self):
        self.x_click(self.header_caracteristicas)
        return Features_page(self.driver)

    def click_header_sobre_nosotros(self):
        self.x_click(self.header_sobre_nosotros())
        return About_us_page(self.driver)

    def click_header_registrarse(self):
        self.x_click(self.header_resgistrarse)
        return Registration_page(self.driver)

    def click_header_ingresar(self):
        self.x_click(self.header_ingresar)
        return Login_page(self.driver)

    def click_header_mis_pacientes(self):
        self.x_click(self.log_header_mis_pacientes)
        return Dashboard_pacientes_page(self.driver)

    def click_header_mis_sesiones(self):
        self.x_click(self.log_header_mis_sesiones)
        return Dashboard_sesiones_page(self.driver)

    def click_header_contactenos(self):
        self.x_click(self.header_contactenos)
        return Contact_us_page(self.driver)

    def click_header_cerrar(self):
        self.x_click(self.log_header_cerrar)

    def click_footer_ayuda(self):
        self.x_click(self.footer_ayuda)
        return Help_page(self.driver)