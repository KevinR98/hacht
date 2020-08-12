
import time
from django.test import TestCase
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
        page = self.page

        page = page.click_header_ingresar()
        page.iniciar_sesion('correo@email.com', '12345', False)
        time.sleep(3)

        self.assertEquals('http://127.0.0.1:8000/', page.get_url())


    def test_caso_prueba_7(self):
        page = self.page

        page = page.click_header_ingresar()
        page.iniciar_sesion('correo@email.com', '12345', True)
        time.sleep(3)
        page.driver.close()

        self.page = Index_page(page.driver)
        page = self.page
        page.driver = webdriver.Firefox()
        page.go_to('http://127.0.0.1:8000/')

        self.assertTrue(page.find_element_x_path(page.user_email_text))

    def test_caso_prueba_8(self):
        page = self.page

        page = page.click_header_ingresar()
        page.iniciar_sesion('correo@email.com', '12345', False)
        time.sleep(3)
        page.driver.close()

        self.page = Index_page(page.driver)
        page = self.page
        page.driver = webdriver.Firefox()
        page.go_to('http://127.0.0.1:8000/')
        page.driver.quit()

        self.assertTrue(not page.find_element_x_path(page.user_email_text))


    def test_caso_prueba_9(self):
        page = self.page

        page = page.click_header_ingresar()
        page.iniciar_sesion('correo@email.com', '12345', False)
        time.sleep(3)

        page = Index_page(page.driver)
        page.go_to('http://127.0.0.1:8000/')
        page.click_header_cerrar()
        time.sleep(3)

        self.assertEquals('http://127.0.0.1:8000/', page.get_url())
        self.assertTrue(not page.find_element_x_path(page.user_email_text))

    def test_caso_prueba_10(self):
        page = self.page

        page = page.click_header_contactenos()
        page.enviar_mensaje('nombre', 'Asunto de prueba',
                                    'correo@email.com', 'Este es un mensaje de prueba')
        time.sleep(3)
        self.assertTrue(page.find_element_x_path(page.modal_success))

    def test_caso_prueba_11(self):
        index_p = self.page
        help_p = index_p.click_footer_ayuda()
        self.assertEquals('http://127.0.0.1:8000/help/', help_p.get_url())

    def test_caso_prueba_12(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('medico@email.com', '12345', False)
        time.sleep(3)

        page = Index_page(page.driver)
        page = page.click_header_mis_pacientes()

        self.assertEquals('http://127.0.0.1:8000/dashboard_pacientes/', page.get_url())

    def test_caso_prueba_16(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('medico@email.com', '12345', False)
        time.sleep(3)

        page = Index_page(page.driver)
        page = page.click_header_mis_pacientes()
        page = page.click_paciente_sesiones()

        self.assertEquals('http://127.0.0.1:8000/dashboard_sesiones/?id_paciente=0', page.get_url())


    def test_caso_prueba_20(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('investigador@email.com', '12345', False)
        time.sleep(3)

        page.go_to('http://127.0.0.1:8000/dashboard_pacientes/')
        self.assertTrue(page.find_element_x_path(page.element_error))



    def test_caso_prueba_21(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('investigador@email.com', '12345', False)
        time.sleep(3)

        page = Index_page(page.driver)
        page.click_header_mis_sesiones()

        self.assertEquals('http://127.0.0.1:8000/dashboard_sesiones/', page.get_url())

    def test_caso_prueba_24(self):
        page = self.page
        page.go_to('http://127.0.0.1:8000/dashboard_sesiones/')
        self.assertTrue(page.find_element_x_path(page.element_error))

    def test_caso_prueba_25(self):
        page = self.page
        page.go_to('http://127.0.0.1:8000/dashboard_pacientes/')
        self.assertTrue(page.find_element_x_path(page.element_error))

    def test_caso_prueba_26(self):
        page = self.page

        self.assertTrue(page.find_element_x_path(page.hacht_logo))
        self.assertTrue(page.find_element_x_path(page.header_demo).text == 'DEMO')
        self.assertTrue(page.find_element_x_path(page.header_contactenos).text == 'CONTACTENOS')
        self.assertTrue(page.find_element_x_path(page.header_sobre_nosotros).text == 'SOBRE NOSOTROS')
        self.assertTrue(page.find_element_x_path(page.header_ingresar).text == 'INGRESAR')
        self.assertTrue(page.find_element_x_path(page.header_resgistrarse).text == 'REGISTRARSE')
        self.assertTrue(page.find_element_x_path(page.header_ayuda).text == 'AYUDA')


    def test_caso_prueba_27(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('medico@email.com', '12345', False)
        time.sleep(3)
        page = Index_page(page.driver)

        self.assertTrue(page.find_element_x_path(page.hacht_logo))
        self.assertTrue(page.find_element_x_path(page.log_header_mis_pacientes).text == 'MIS PACIENTES')
        self.assertTrue(page.find_element_x_path(page.log_header_ayuda).text == 'AYUDA')
        self.assertTrue(page.find_element_x_path(page.log_header_demo).text == 'DEMO')
        self.assertTrue(page.find_element_x_path(page.log_header_contactenos).text == 'CONTACTENOS')
        self.assertTrue(page.find_element_x_path(page.log_header_sobre_nosotros).text == 'SOBRE NOSOTROS')
        self.assertTrue(page.find_element_x_path(page.log_header_cerrar).text == 'CERRAR')



    def test_caso_prueba_28(self):
        page = self.page
        page = page.click_header_ingresar()
        page.iniciar_sesion('investigador@email.com', '12345', False)
        time.sleep(3)
        page = Index_page(page.driver)

        self.assertTrue(page.find_element_x_path(page.hacht_logo))
        self.assertTrue(page.find_element_x_path(page.log_header_mis_sesiones).text == 'MIS SESIONES')
        self.assertTrue(page.find_element_x_path(page.log_header_ayuda).text == 'AYUDA')
        self.assertTrue(page.find_element_x_path(page.log_header_demo).text == 'DEMO')
        self.assertTrue(page.find_element_x_path(page.log_header_contactenos).text == 'CONTACTENOS')
        self.assertTrue(page.find_element_x_path(page.log_header_sobre_nosotros).text == 'SOBRE NOSOTROS')
        self.assertTrue(page.find_element_x_path(page.log_header_cerrar).text == 'CERRAR')
