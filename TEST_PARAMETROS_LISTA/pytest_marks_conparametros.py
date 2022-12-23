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

t = 0.5


def get_data():
    return [
        ("fede", "123123"),
        ("fede", "123123"),
        ("cappoo", "55555"),
        ("admin", "admin123"),
    ]


@pytest.mark.parametrize("user,contraseña", get_data())
def test_login(user, contraseña):
    global driver
    service = Service(r"chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    f = Funciones(driver)
    f.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)

    f.texto_agregar_validar("xpath", "//input[@name='username']", user, t)
    f.texto_agregar_validar("xpath", "//input[@type='password']", contraseña, t)
    f.clickear("xpath", "//button[@type='submit']", t)
    print(f"{f.ahora()}: Entrando al sistema")
    driver.close()
