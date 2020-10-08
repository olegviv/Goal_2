import pytest
from pages.hamburger_menu import HamburgerMenu
from pages.login_page import LoginPage
import time


@pytest.mark.usefixtures("driver")
class TestLogin:
    @pytest.mark.parametrize("login, passwd, rez",
                             [
                                 ("bla_1", "bla1", "Invalid email address"),
                                 ("mtadmin@gmail.com", "", "Please fill in the required field"),
                                 ("", "wrongPass", "Please fill in the required field"),
                             ]
                             )
    def test_login_to_dima_page_object(self, login, passwd, rez):
        self.login_page = LoginPage(self.driver)
        self.hamburger_menu = HamburgerMenu(self.driver)
        self.login_page.open()
        time.sleep(3)
        assert self.login_page.at_page()
        self.login_page.enter_email(login)
        self.login_page.enter_password(passwd)
        self.login_page.click_login_button()
        assert self.login_page.wait_for_text_to_appear(rez)