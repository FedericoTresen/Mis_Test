import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import datetime
from selenium.webdriver import ActionChains
import pytest
from funciones import Funciones

t = 0.1


# HACE TEST DE TODAS LAS POSIBILIDADES DADAS EN UN LOGIN


def test_login1():
    global driver
    service = Service(r"chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.texto_agregar_validar("xpath", "//input[@id='Email']", "fedeee@yourstore.com", t)
    f.texto_agregar_validar("xpath", "//input[@id='Password']", "federicoo", t)
    f.clickear("xpath", "//input[@id='RememberMe']", t)
    f.clickear("xpath", "//button[@type='submit']", t)
    error1 = f.seleccionar_xpath(
        "//div[@class='message-error validation-summary-errors']"
    )
    error1 = error1.text

    if (
        error1
        == "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
    ):
        print(f"{f.ahora()}: Prueba de validacion exitosa")
    else:
        print(f"{f.ahora()}: La prueba de validacion es incorrecta")
    driver.close()


def test_login2():
    global driver
    service = Service(
        r"C:\Users\fede-\Escritorio\CURSOS-PYTHON\CURSO-API-UDEMY\chromedriver.exe"
    )
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.texto_agregar_validar("xpath", "//input[@id='Email']", "", t)
    f.texto_agregar_validar("xpath", "//input[@id='Password']", "federicoo", t)
    f.clickear("xpath", "//input[@id='RememberMe']", t)
    f.clickear("xpath", "//button[@type='submit']", t)
    error1 = f.seleccionar_xpath("//span[@id='Email-error']")
    error1 = error1.text

    if error1 == "Please enter your email":
        print(f"{f.ahora()}: Prueba de Email vacio exitosa")
    else:
        print(f"{f.ahora()}: Prueba de Email vacio incorrecta")
    driver.close()


def test_login3():
    global driver
    service = Service(
        r"C:\Users\fede-\Escritorio\CURSOS-PYTHON\CURSO-API-UDEMY\chromedriver.exe"
    )
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.texto_agregar_validar("xpath", "//input[@id='Email']", "fedee", t)
    f.texto_agregar_validar("xpath", "//input[@id='Password']", "federicoo", t)
    f.clickear("xpath", "//input[@id='RememberMe']", t)
    f.clickear("xpath", "//button[@type='submit']", t)
    error1 = f.seleccionar_xpath("//span[@id='Email-error']")
    error1 = error1.text

    if error1 == "Wrong email":
        print(f"{f.ahora()}: Prueba de Email incorrecto exitosa")
    else:
        print(f"{f.ahora()}: Prueba de Email incorrecto fallida")
    driver.close()


def test_login4():
    global driver
    service = Service(
        r"C:\Users\fede-\Escritorio\CURSOS-PYTHON\CURSO-API-UDEMY\chromedriver.exe"
    )
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.texto_agregar_validar("xpath", "//input[@id='Email']", "admin@yourstore.com", t)
    f.texto_agregar_validar("xpath", "//input[@id='Password']", "admin", t)
    f.clickear("xpath", "//input[@id='RememberMe']", t)
    f.clickear("xpath", "//button[@type='submit']", t)
    existe = f.existe("xpath", "//h1[contains(.,'Dashboard')]", t)

    if existe == "existe":
        print(f"{f.ahora()}: Prueba de Email y contraseña correcta exitosa")
    else:
        print(f"{f.ahora()}: Prueba de Email y contraseña correcta fallida")
    driver.close()
