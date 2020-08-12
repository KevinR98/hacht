
from .dashboard_sesiones import Dashboard_sesiones_page
from ..Base import Base

class Dashboard_pacientes_page(Base):

    def __init__(self):
        self.paciente_sesiones = '/html/body/main/section/div[2]/div/div[1]/div/div/div[2]/div[2]/a/span'

        super(Dashboard_pacientes_page, self).__init__(Base.firefox_webdriver(self))

    def click_paciente_sesiones(self):
        self.x_click(self.paciente_sesiones)
        return Dashboard_sesiones_page(self.driver)

