from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_INPUT = (By.XPATH, "//input[@autocomplete='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@autocomplete='current-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/button/span[1]/span")
    