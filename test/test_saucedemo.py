import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.funciones import configuracion, login, contador_de_productos, añadir_carrito, entrar_carrito

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

def test_cantidad_productos(driver_conf):
    login(driver_conf)
    cantidad = contador_de_productos(driver_conf)
    assert cantidad > 0

def test_elementos_interfaz(driver_conf):
    login(driver_conf)
    menu = driver_conf.find_element(By.ID, "react-burger-menu-btn").text
    assert menu == "Open Menu"
    sort = driver_conf.find_element(By.CLASS_NAME, "active_option").text
    assert sort == "Name (A to Z)"

def test_añadir_carrito(driver_conf):
    login(driver_conf)
    añadir_carrito(driver_conf)
    carrito = driver_conf.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(carrito) > 0

def test_validar_carrito(driver_conf):
    login(driver_conf)
    añadir_carrito(driver_conf)
    entrar_carrito(driver_conf)
    primerElemento = driver_conf.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert primerElemento == "Sauce Labs Backpack"

