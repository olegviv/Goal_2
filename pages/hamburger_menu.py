from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Locators.hamburger_menu_locators import HamburgerMenuLocators


class HamburgerMenu:



    def __init__(self, driver):
        self.driver = driver
        self.hamburger_menu = HamburgerMenuLocators()

    def at_menu(self):
        time.sleep(2)
        self.driver.find_element(*self.hamburger_menu.HAMBURGER_BUTTON).click()
        time.sleep(5)
        try:
            profile_logo_element = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Simplicity']")))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False