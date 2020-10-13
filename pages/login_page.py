import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from Locators.login_page_locators import LoginPageLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPageLocators()

    def login_to_dima(self):
        time.sleep(2)
        self.driver.find_element(*self.login.LOGIN_INPUT).send_keys("unfold@gmail.com")
        self.driver.find_element(*self.login.PASSWORD_INPUT).send_keys("u*6h8pKG")
        self.driver.find_element(*self.login.LOGIN_BUTTON).submit()

    def enter_email(self, user_name):
        self.driver.find_element(*self.login.LOGIN_INPUT).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(*self.login.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login.LOGIN_BUTTON)).click()

    def at_page(self):
        return "Dima.Motion App" in self.driver.title

    def open(self):
        self.driver.get("https://dima-motion.simplicity-development.de/")
        return self

    def wait_for_text_to_appear(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'" + text + "')]")))

