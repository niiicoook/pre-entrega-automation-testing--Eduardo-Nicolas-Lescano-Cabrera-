import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.funciones import configuracion, login

@pytest.fixture
def driver_conf():
    driver = configuracion()
    yield driver
    driver.quit()

def test_login(driver_conf):
    login(driver_conf)
    assert "/inventory.html" in driver_conf.current_url
    titulo = driver_conf.find_element(By.CLASS_NAME, "title").text

    assert titulo == "Products"

