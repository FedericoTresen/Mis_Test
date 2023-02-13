import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from funciones import Funciones
from allure_commons.types import AttachmentType

t = 0.5

# GENERAR REPORTE ALLURE: pytest .\TEST_JMETER.py --alluredir="./allurereports/TEST_JMETER"
# ABRIR REPORTE ALLURE: allure serve .\allurereports\TEST_JMETER


def test_login1():
    global driver
    service = Service(r"chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.texto_agregar_validar("id", "Email", "admin@yourstore.com", t)
    f.texto_agregar_validar("id", "Password", "admin", t)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="logueo",
        attachment_type=AttachmentType.PNG,
    )
    f.clickear("xpath", "//button[@type='submit']", t)
    f.clickear("xpath", "(//p[contains(.,'Customers')])[1]", t)
    f.clickear("xpath", "(//p[contains(.,'Customers')])[2]", t)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="customers",
        attachment_type=AttachmentType.PNG,
    )
    f.clickear("xpath", "//a[contains(.,'Add new')]", t)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="agregar_nuevo",
        attachment_type=AttachmentType.PNG,
    )
    f.texto_agregar_validar("id", "Email", "emailgenerico@gmail.com", t)
    f.texto_agregar_validar("id", "Password", "contraseña", t)
    f.texto_agregar_validar("id", "FirstName", "Federico", t)
    f.texto_agregar_validar("id", "LastName", "Tresen", t)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="llenando_campos",
        attachment_type=AttachmentType.PNG,
    )
    f.clickear("id", "Gender_Male", t)
    f.texto_agregar_validar("id", "DateOfBirth", "1/2/1994", t)
    f.texto_agregar_validar("id", "Company", "OSPAV", t)
    f.clickear("id", "IsTaxExempt", t)
    f.clickear("xpath", "(//input[@tabindex='0'])[1]", t)
    f.clickear("xpath", "(//li[@tabindex='-1'])[2]", t)
    f.clickear("xpath", "(//div[@unselectable='on'])[4]", t)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="llenando_campos2",
        attachment_type=AttachmentType.PNG,
    )
    f.clickear("xpath", "//li[contains(.,'Administrators')]", t)
    f.clickear("xpath", "//select[@id='VendorId']", t)
    f.seleccionar("xpath", "//select[@id='VendorId']", "index", 2, t)
    f.texto_agregar_validar(
        "id", "AdminComment", "esto es un comentario del administrador", t
    )
    allure.attach(
        driver.get_screenshot_as_png(),
        name="llenando_campos3",
        attachment_type=AttachmentType.PNG,
    )
    f.clickear("xpath", "//button[@name='save']", t)
    f.salida()
    driver.close()
