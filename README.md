
# Proyecto de automatización de pruebas

El objetivo de este proyecto es automatizar la ejecucion de pruebas que se hacen en la pagina www.saucedemo.com.
Las pruebas cubre el fujo normal de compra, valida el inicio de sesión, agrega al carrito elementos y valida su exitencia en el mismo. 
El proyecto sirve como ejemplo práctico de automatización de pruebas web, demostrando buenas prácticas en el uso de Selenium WebDriver con Python y la organización de tests con Pytest.



## Lenguaje y librerias utilizadas:


- Python: Lenguaje de programación
- Pytest: Framework de testing
- Selenium: Herramienta de automatización 


## Instalacion de dependencias

Es necesario poseer python 3 y Chrome ya instalados.

#### 1. Clonar proyecto.

```bash
git clone https://github.com/niiicoook/pre-entrega-automation-testing--Eduardo-Nicolas-Lescano-Cabrera-.git
cd pre-entrega-automation-testing--Eduardo-Nicolas-Lescano-Cabrera-
```
#### 2. Crear entorno virtual
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

```

#### 3. Instalar dependencias
```bash
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager

```
## Como ejecutar las pruebas
#### Ejecutar todos los suits de prueba

```bash
pytest tests/test_saucedemo.py
```

#### Ejecutar test especificop
```bash
pytest funcion() -k
```

#### Generar reporte html
```bash
pytest --html=report.html
```

##### Notas:
-  Las pruebas utilizan las credenciales del usuario ***standard_user*** con contraseña ***secret_sauce***
- Cada prueba es independiente y cierra el navegador automáticamente al finalizar 
- El WebDriver Manager descarga automáticamente la versión correcta de ChromeDriver en la primera ejecución
