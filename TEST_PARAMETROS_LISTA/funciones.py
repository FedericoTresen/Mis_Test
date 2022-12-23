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


class Funciones:
    def __init__(self, driver):
        self.driver = driver

    # AGREGA TIEMPO ENTRE CADA ACCION
    def tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    # OBTIENE FECHA Y HORA DE LA ACCION
    def ahora(self):
        ahora = datetime.datetime.now()
        ahora = ahora.strftime(("%d/%m/%Y %H:%M:%S"))
        ahora = str(ahora)
        return ahora

    # ABRE UNA URL EN EL NAVEGADOR
    def navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()

        print(f"{self.ahora()}: Pagina abierta:   {str(url)} ")
        t = time.sleep(tiempo)
        return t

    # ---------------------SELECCIONAR POR XPATH Y POR ID-----------------------------------------------------------
    def seleccionar_xpath(self, selector):
        val = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, selector))
        )
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, selector)
        print(f"{self.ahora()}: se ha seleccionado el campo: {selector}")
        return val

    def seleccionar_id(self, selector):
        val = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, selector))
        )
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, selector)
        print(f"{self.ahora()}: se ha seleccionado el campo: {selector}")
        return val



    # ---------------------AGREGAR TEXTO EN CAMPOS-----------------------------------------------------------
    # VALIDA UN CAMPO DE TEXTO Y AGREGA UNO EN EL MISMO

    def texto_agregar_validar(self, xpath_o_id, selector, texto, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.clear()  # si el campo en la pagina tiene algo escrito lo borra
                val.send_keys(texto)
                print(
                    f"{self.ahora()}: Escribiendo en el campo {selector} el texto: {texto} "
                )
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val.clear()  # si el campo en la pagina tiene algo escrito lo borra
                val.send_keys(texto)
                print(
                    f"{self.ahora()}: Escribiendo en el campo {selector} el texto: {texto} "
                )
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    # ---------------------CLICKEAR-----------------------------------------------------------

    def clickear(self, xpath_o_id, selector, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.click()
                print(f"{self.ahora()}: Damos click en el campo: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val.click()
                print(f"{self.ahora()}: Damos click en el campo: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    # ---------------------INDICA CUANDO TERMINA EL TEST-----------------------------------------------------------
    def salida(self):
        print(f"{self.ahora()}: Se ha finalizado el test")

    # ---------------------SELECCIONA EN LISTADOS DESPLEGABLES-----------------------------------------------------------

    def seleccionar(self, xpath_o_id, selector, texto_index_value, dato, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val = Select(val)
                if texto_index_value == "text":
                    val.select_by_visible_text(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por texto, el texto elegido fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                elif texto_index_value == "index":
                    val.select_by_index(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por indice, el indice elegido fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                elif texto_index_value == "value":
                    val.select_by_value(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por valor, el valor elegido fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: {selector}")
                return t
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val = Select(val)
                if texto_index_value == "text":
                    val.select_by_visible_text(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por texto, el texto elegido fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                elif texto_index_value == "index":
                    val.select_by_index(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por indice, el indice elegido fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                elif texto_index_value == "value":
                    val.select_by_value(dato)
                    print(
                        f"{self.ahora()}: El campo fue seleccionado por valor, el dato valor fue: {dato}"
                    )
                    t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: {selector}")
                return t
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    # ---------------------SUBE ARCHIVOS-----------------------------------------------------------

    def upload(self, xpath_o_id, selector, ruta, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.send_keys(ruta)
                print(f"{self.ahora()}: se sube el archivo: {ruta}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val.send_keys(ruta)
                print(f"{self.ahora()}: se sube el archivo: {ruta}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

# ---------------------CHECKBOX-----------------------------------------------------------

    # TILDA LAS CHECKBOX

    def checkbox(self, xpath_o_id, selector, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.click()
                print(f"{self.ahora()}: click en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val.click()
                print(f"{self.ahora()}: click en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
                return t
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    # TILDA LAS CHECKBOX DE MANERA MULTIPLE

    def checkbox_multiple(self, xpath_o_id, tiempo, *args):
        if xpath_o_id == "xpath":
            try:
                for argumento in args:
                    val = self.seleccionar_xpath(argumento)
                    val.click()
                    print(f"{self.ahora()}: click en el elemento: {argumento}")
                    t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + argumento)
                return t
        elif xpath_o_id == "id":
            try:
                for argumento in args:
                    val = self.seleccionar_id(argumento)
                    val.click()
                    print(f"{self.ahora()}: click en el elemento: {argumento}")
                    t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + argumento)
                return t
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")





# ---------------------CHECK EXIST-----------------------------------------------------------

    def existe(self, xpath_o_id, selector, tiempo):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                print(f"El elemento: {selector} existe")
                t = time.sleep(tiempo)
                return "existe"
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora}: No se encontro el elemento: {selector}")
                return "no existe"
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                print(f"El elemento: {selector} existe")
                t = time.sleep(tiempo)
                return "existe"
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora}: No se encontro el elemento: {selector}")
                return "no existe"
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")


 # ---------------------DOUBLE CLICK-----------------------------------------------------------


    def double_click(self, xpath_o_id, selector, tiempo=.2):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.clear()  # si el campo en la pagina tiene algo escrito lo borra
                accion = ActionChains(self.driver)
                accion.double_click(val).perform()
                print(f"{self.ahora()}: Se ha dado doble click en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                accion = ActionChains(self.driver)
                accion.double_click(val).perform()
                print(f"{self.ahora()}: Se ha dado doble click en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    # ---------------------CLICK DERECHO-----------------------------------------------------------

    def click_derecho(self, xpath_o_id, selector, tiempo=.2):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val.clear()  # si el campo en la pagina tiene algo escrito lo borra
                accion = ActionChains(self.driver)
                accion.context_click(val).perform()
                print(f"{self.ahora()}: Se ha dado click derecho en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                accion = ActionChains(self.driver)
                accion.context_click(val).perform()
                print(f"{self.ahora()}: Se ha dado click derecho en el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

# ---------------------ARRASTRAR Y SOLTAR----------------------------------------------------------

    def arrastrar_soltar(self, xpath_o_id, selector, destino, tiempo=.2):
        if xpath_o_id == "xpath":
            try:
                val = self.seleccionar_xpath(selector)
                val2 = self.seleccionar_xpath(destino)
                accion = ActionChains(self.driver)
                accion.drag_and_drop(val,val2).perform()
                print(f"{self.ahora()}: Se arrastro el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                val = self.seleccionar_id(selector)
                val2 = self.seleccionar_id(destino)
                accion = ActionChains(self.driver)
                accion.drag_and_drop(val,val2).perform()
                print(f"{self.ahora()}: Se arrastro el elemento : {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")




    def arrastrar_x_y(self, xpath_o_id, selector, x, y,  tiempo=.2):
        if xpath_o_id == "xpath":
            try:
                self.driver.switch_to.frame(0)
                val = self.seleccionar_xpath(selector)
                accion = ActionChains(self.driver)
                accion.drag_and_drop_by_offset(val, x, y).perform()
                print(f"{self.ahora()}: Se arrastro el elemento: {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                self.driver.switch_to.frame(0)
                val = self.seleccionar_id(selector)
                accion = ActionChains(self.driver)
                accion.drag_and_drop_by_offset(val, x, y).perform()
                print(f"{self.ahora()}: Se arrastro el elemento : {selector}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

    def click_x_y(self, xpath_o_id, selector, x, y, tiempo=.2):
        if xpath_o_id == "xpath":
            try:
                #self.driver.switch_to.frame(0)
                val = self.seleccionar_xpath(selector)
                accion = ActionChains(self.driver)
                accion.move_to_element_with_offset(val, x, y).click().perform()
                print(f"{self.ahora()}: Click al elemento : {selector}, coordenada {x} {y}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        elif xpath_o_id == "id":
            try:
                #self.driver.switch_to.frame(0)
                val = self.seleccionar_id(selector)
                accion = ActionChains(self.driver)
                accion.move_to_element_with_offset(val, x, y).click().perform()
                print(f"{self.ahora()}: Click al elemento : {selector}, coordenada {x} {y}")
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"{self.ahora()}: no se ha encontrado el elemento: " + selector)
        else:
            print(f"El tipo: {xpath_o_id} es incorrecto, tiene que ser xpath o id!")

