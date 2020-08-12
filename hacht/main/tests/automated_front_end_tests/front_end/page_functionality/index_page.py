
from selenium import webdriver
from ..Base import Base

class Index_page(Base):

    def __init__(self):
        self.header_inicio = '/html/body/nav/div/div/ul/li[6]/a'
        self.header_demo = '/html/body/nav/div/div/ul/li[2]/a'
        self.header_caracteristicas = '/html/body/nav/div/div/ul/li[3]/a'
        self.header_sobre_nosotros = '/html/body/nav/div/div/ul/li[4]/a'
        self.header_resgistrarse = '/html/body/nav/div/div/ul/li[5]/a'
        self.header_ingresar = '/html/body/nav/div/div/ul/li[6]/a'

        super(Index_page, self).__init__(Base.firefox_webdriver(self))
        self.driver.get('http://127.0.0.1:8000/')



    def click_header_demo(self):
        self.x_click(self.header_demo)

    def click_header_caracteristicas(self):
        self.x_click(self.header_caracteristicas)

    def click_header_sobre_nosotros(self):
        self.x_click(self.header_sobre_nosotros())

    def click_header_registrarse(self):
        self.x_click(self.header_resgistrarse)

    def click_header_ingresar(self):
        self.x_click(self.header_ingresar)
