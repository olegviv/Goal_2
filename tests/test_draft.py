import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

import time

class TestLogin:

    def test_login_to_Simplicity(self):
        driver = Chrome(ChromeDriverManager().install())
        driver.get("https://dima-motion.simplicity-development.de/")
        assert "Dima.Motion App" in driver.title
        driver.maximize_window()

        driver.find_element_by_xpath("//input[@autocomplete='username']").send_keys("unfold@gmail.com")
        driver.find_element_by_xpath("//input[@autocomplete='current-password']").send_keys("u*6h8pKG")
        driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/form/button/span[1]/span").submit()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='button']").click()


        simplicity_logo_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='Simplicity']")))
        assert simplicity_logo_element.is_displayed()
        driver.close()