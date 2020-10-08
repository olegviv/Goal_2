import pytest
from pages.hamburger_menu import HamburgerMenu
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_to_dima_page_object(self):
        self.login_page = LoginPage(self.driver)
        self.hamburger_menu = HamburgerMenu(self.driver)
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_dima()
        assert self.hamburger_menu.at_menu()
