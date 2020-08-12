
import os
from django.conf import settings
from django.test import TestCase
from selenium import webdriver

from ..page_functionality.index_page import Index_page


class LoginTestCase(TestCase):

    def setUp(self):
        self.index = Index_page()

        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.index.driver.quit()
        super(LoginTestCase, self).tearDown()

    def test_header(self):
        page = self.index
        page.click_login()
        self.assertEquals('http://127.0.0.1:8000/login/', page.get_url())
