
from selenium import webdriver
from ..Base import Base

class Demo_page(Base):

    def __init__(self):
        self.image_0 = '/html/body/main/div/div[3]/div[1]/div/div[1]/a[1]/img'
        self.card_image_selected = '//*[@id="card"]'
        self.card_boton_analizar = '/html/body/main/div/div[3]/div[2]/div/div/form/input[4]'
        self.card_prediccion_texto = '/html/body/main/div/div[3]/div[2]/div/div/p[2]'

        super(Demo_page, self).__init__(Base.firefox_webdriver(self))


