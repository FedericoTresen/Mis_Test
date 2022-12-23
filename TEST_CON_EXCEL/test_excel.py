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
from funciones import Funciones
from funciones_excel import Funexcel

t = 0.1


# RECIBE VALORES DE UN ARCHIVO .XLSX Y HACE EL TEST CON ELLOS


class BaseTest(unittest.TestCase):
    def setUp(self):
        service = Service(r"chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test_login1(self):
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.navegar("https://demoqa.com/text-box", t)
        ruta = r"C:\Users\fede-\Escritorio\CURSOS-PYTHON\CURSO-API-UDEMY\excel\datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Sheet1")

        for r in range(2, filas + 1):
            nombre = fe.readData(ruta, "Sheet1", r, 1)
            email = fe.readData(ruta, "Sheet1", r, 2)
            direccion1 = fe.readData(ruta, "Sheet1", r, 3)
            direccion2 = fe.readData(ruta, "Sheet1", r, 4)

            f.texto_agregar_validar("id", "userName", nombre, t)
            f.texto_agregar_validar("id", "userEmail", email, t)
            f.texto_agregar_validar("id", "currentAddress", direccion1, t)
            f.texto_agregar_validar("id", "permanentAddress", direccion2, t)
            f.clickear("id", "submit", t)

            e = f.existe("id", "name", t)
            if e == "existe":
                print("Elemento insertado correctamente")
                fe.writeData(ruta, "Sheet1", r, 5, "Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Sheet1", r, 5, "Error")
