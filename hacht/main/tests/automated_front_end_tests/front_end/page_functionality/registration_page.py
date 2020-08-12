
from selenium import webdriver
from ..Base import Base

class Registration_page(Base):

    def __init__(self, driver):
        self.input_nombre = '//*[@id="id_nombre"]'
        self.input_email = '//*[@id="email"]'
        self.input_contrasena = '//*[@id="id_password"]'

        self.dropdown_rol = '//*[@id="id_rol"]'
        self.dropdown_rol_medico = '/html/body/main/section/div/form/div[4]/select/option[1]'
        self.dropdown_rol_investigador = '/html/body/main/section/div/form/div[4]/select/option[2]'

        self.input_organizacion = '//*[@id="id_org"]'
        self.input_uso = '//*[@id="id_uso"]'
        self.boton_submit = '/html/body/main/section/div/form/button'

        self.modal_success = '/html/body/div/div/div[1]'
        self.error_message = '/html/body/main/section/div/form/label[3]'



        super(Registration_page, self).__init__(driver)

    def registrarse(self, nombre, email, contrasena, rol, org, uso):
        self.x_write_entry(nombre, self.input_nombre)
        self.x_write_entry(email, self.input_email)
        self.x_write_entry(contrasena, self.input_contrasena)

        if rol == 'medico':
            self.x_click(self.dropdown_rol_medico)
        elif rol == 'investigador':
            self.x_click(self.dropdown_rol_investigador)

        self.x_write_entry(org, self.input_organizacion)
        self.x_write_entry(uso, self.input_uso)

        self.x_click(self.boton_submit)