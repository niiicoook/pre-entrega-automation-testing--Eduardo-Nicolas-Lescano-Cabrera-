from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def configuracion():
    """
    configuracion() crea el buscador que se va a utilizar. 
    service es para que siempre se este usando el manager de Chrome mas reciente.
    driver es la variable que se va a usar para trabajar con el buscador.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def login(driver):
    """
    login() recive como parametro driver que es el buscador que se acaba de crear en configuracion()
    driver.get(URL) es para dirigirnos a la url de la pagina en la cual vamos a trabajar
    wait es una variable para almacenar el WebDriverWait, este sirve para que la pagina espere cierto tiempo, en wait.until le pido que
    espere hasta que aparezca el elemento cuya id sea "user-name", si lo encuentra antes de los 10 sec avanza, de lo contrario tira error.

    los find_element() buscan en el contenido html, en ese caso segun ID y con send_keys() les paso los parametros antes establecidos. Con click() 
    le doy al boton de logueo

    el ultimo wait espera que la url contenga /inventory.html, con esto valido estar en la pagina deseada
    """
    driver.get(URL)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("/inventory.html"))

def contador_de_productos(driver):
    """
    contador_de_productos() recibe el buscador como parametro.
    En productos, guardo la lista de elementos que me da find_elements(), cuyos son aquellos con class = "inventory_item"
    Retorno len(productos) que es igual a la cantidad de elementos que veo en pantalla 
    """
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    return len(productos)

def añadir_carrito(driver):
    """
    añadir_carrito() recibe al buscador como parametro. find_element() busca el boton de añadir al carrito mediante su id y .click() es para apretar el boton
    """
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

def entrar_carrito(driver):
    """
    entrar_carrito() recibe al buscador como parametro. find_element() busca el boton de carrito .click() es para apretar el boton
    """
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()



