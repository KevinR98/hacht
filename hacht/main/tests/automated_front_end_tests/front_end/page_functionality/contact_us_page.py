
from ..Base import Base

class Contact_us_page(Base):

    def __init__(self, driver):

        self.form_nombre = '//*[@id="id_nombre"]'
        self.form_asunto = '//*[@id="id_asunto"]'
        self.form_email = '//*[@id="email"]'
        self.form_mensaje = '//*[@id="id_mensaje"]'
        self.form_boton_enviar = '/html/body/main/section/div/form/div[5]/button'

        self.modal_success = '/html/body/div/div/div[1]'

        super(Contact_us_page, self).__init__(driver)

    def enviar_mensaje(self, nombre, asunto, email, mensaje):
        self.x_write_entry(nombre, self.form_nombre)
        self.x_write_entry(asunto, self.form_asunto)
        self.x_write_entry(email, self.form_email)
        self.x_write_entry(mensaje, self.form_mensaje)

        self.x_click(self.form_boton_enviar)

