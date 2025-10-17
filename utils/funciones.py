from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def configuracion():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def login(driver):
    driver.get(URL)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("/inventory.html"))

def contador_de_productos(driver):

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    return len(productos)

def añadir_carrito(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

def entrar_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


driver = configuracion()
login(driver)
contador_de_productos(driver)
añadir_carrito(driver)
entrar_carrito(driver)



# time.sleep(2)
# driver.quit()