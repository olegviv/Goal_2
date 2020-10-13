import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome


@pytest.fixture()
def driver(request):
    driver = Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    yield driver
    driver.quit()
