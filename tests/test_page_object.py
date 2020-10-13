import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.hamburger_menu import HamburgerMenu
from pages.login_page import LoginPage

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.hamburger_menu = HamburgerMenu(self.driver)

    def test_login_to_dima_page_object(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_dima()
        assert self.hamburger_menu.at_menu()

    def teardown_method(self):
        self.driver.close()