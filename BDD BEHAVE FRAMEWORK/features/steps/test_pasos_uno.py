from behave import *
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
import unittest
from funciones import Funciones

t = 0.5


@given("abriendo el navegador")
def step_impl(context):
    print("STEP: Given abriendo el navegador")
    global driver, f
    service = Service(r"chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    f = Funciones(context.driver)
    f.navegar("https://demoqa.com/text-box", 1)


@when('cargando el nombre del usuario "{usuario}"')
def step_impl(context, usuario):
    print("STEP: When cargando el nombre del usuario")
    f.texto_agregar_validar("id", "userName", usuario, t)


@then('cargando su email "{email}"')
def step_impl(context, email):
    print("STEP: Then cargando su email")
    f.texto_agregar_validar("id", "userEmail", email, t)


@then('cargando su direccion1 "{direccion1}"')
def step_impl(context, direccion1):
    print("STEP: Then cargando su direccion 1")
    f.texto_agregar_validar("id", "currentAddress", direccion1, t)


@then('cargando su direccion2 "{direccion2}"')
def step_impl(context, direccion2):
    print("STEP: Then cargando su direccion 2")
    f.texto_agregar_validar("id", "permanentAddress", direccion2, t)
    f.clickear("id", "submit", t)
    context.driver.close()
