
import time
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from ..page_functionality.index_page import Index_page


class LoginTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
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

        self.assertTrue(register_p.find_element_x_path(register_p.modal_success))

    def test_caso_prueba_2(self):
        index_p = self.page
        register_p = index_p.click_header_registrarse()
        register_p.registrarse("", "fgr@email.com", '12345', 'medico', 'Empresa', 'Prueba')

        #time.sleep(5)
        self.assertTrue(register_p.find_element_x_path(register_p.error_message))

    def test_caso_prueba_3(self):
        self.page.click_header_demo()
        self.assertEquals("http://127.0.0.1:8000/demo/", self.page.get_url())

    def test_caso_prueba_4(self):
        index_p = self.page
        demo_p = index_p.click_header_demo()
        demo_p.x_click(demo_p.image_0)

        self.assertTrue(demo_p.find_element_x_path(demo_p.card_image_selected))

    def test_caso_prueba_5(self):
        index_p = self.page
        demo_p = index_p.click_header_demo()
        demo_p.x_click(demo_p.image_0)

        self.wait.until(ec.visibility_of_element_located((By.XPATH, demo_p.card_image_selected)))
        demo_p.x_click(demo_p.card_boton_analizar)

        self.assertTrue(demo_p.find_element_x_path(demo_p.card_prediccion_texto))


    def test_caso_prueba_6(self):
        index_p = self.page

        current_p = index_p.click_header_ingresar()
        current_p = current_p.iniciar_sesion('correo@email.com', '12345')

        self.assertEquals('http://127.0.0.1:8000/', current_p.get_url())

    #Funcionalidad ya no existe
    def test_caso_prueba_7(self):
        index_p = self.page

        current_p = index_p.click_header_ingresar()
        current_p = current_p.iniciar_sesion('correo@email.com', '12345')

        current_p.driver.close()
        current_p.driver = webdriver.Firefox()
        current_p.go_to('http://127.0.0.1:8000/')

        self.assertTrue(current_p.find_element_by_xpath(current_p.log_header_cerrar))

    #Funcionalidad ya no existe
    def test_caso_prueba_8(self):
        index_p = self.page

        current_p = index_p.click_header_ingresar()
        current_p = current_p.iniciar_sesion('correo@email.com', '12345')

        current_p.driver.close()
        current_p.driver = webdriver.Firefox()
        current_p.go_to('http://127.0.0.1:8000/')

        self.assertTrue(not current_p.find_element_by_xpath(current_p.log_header_cerrar))

    def test_caso_prueba_9(self):
        index_p = self.page

        current_p = index_p.click_header_ingresar()
        current_p = current_p.iniciar_sesion('correo@email.com', '12345')

        current_p.click_header_cerrar()

        self.assertEquals('http://127.0.0.1:8000/', current_p.get_url())
        self.assertTrue(not current_p.find_element_by_xpath(current_p.user_email_text))

    def test_caso_prueba_10(self):
        index_p = self.page

        contact_us_p = index_p.click_header_contactenos()
        contact_us_p.enviar_mensaje('nombre', 'Asunto de prueba',
                                    'correo@email.com', 'Este es un mensaje de prueba')
        