from selenium import webdriver

class Base:

    def __init__(self, webdriver):
        self.element_error = '/html/body/main/section/div/div/h2'
        self.driver = webdriver

    def firefox_webdriver(self):
        return webdriver.Firefox()

    def go_to(self, locator):
        self.driver.get(locator)

    def find_element_x_path(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            return False

    def x_click(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def x_write_entry(self, text, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(text)

    def get_url(self):
        url = self.driver.current_url
        return url

