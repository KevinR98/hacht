
import time
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from selenium import webdriver

from ..page_functionality.contact_us_page import Contact_us_page
from ..page_functionality.dashboard_pacientes import Dashboard_pacientes_page
from ..page_functionality.dashboard_sesiones import Dashboard_sesiones_page
from ..page_functionality.demo_page import Demo_page
from ..page_functionality.features_page import Features_page
from ..page_functionality.help_page import Help_page
from ..page_functionality.index_page import Index_page
from ..page_functionality.login_page import Login_page
from ..page_functionality.registration_page import Registration_page

class LoginTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Index_page(self.driver)
        self.page.go_to('http://127.0.0.1:8000/')

        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.page.driver.quit()
        super(LoginTestCase, self).tearDown()


    def test_caso_prueba_1(self):
        index_p = self.page
        register_p = index_p.click_header_registrarse()
        register_p.registrarse("Nombre", "fgr@email.com", '12345', 'medico', 'Empresa', 'Prueba')

        time.sleep(5)
        self.assertTrue(register_p.find_element_x_path(register_p.modal_success))


    def test_caso_prueba_2(self):
        index_p = self.page

        login_p = index_p.click_header_ingresar()
        login_p.iniciar_sesion('usuario', '12345')
