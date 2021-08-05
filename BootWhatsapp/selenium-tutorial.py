# -*- coding: utf-8 -*-
"""
Selenium es un programa de automatización de boot para el navegador
"""
from selenium import webdriver # Modulo que provee todas las implementaciones
import time # Se usa para agregar demora en la ejecución de un programa

"""
pip install webdriver-manager 
"""
# Importamos
from webdriver_manager.chrome import ChromeDriverManager 
# Usamos el controlador para que se se ejecute o instale
driver = webdriver.Chrome(ChromeDriverManager().install())
# Abre la pagina que deseamos visitar
driver.get('https://www.python.org/')
# Tiempo de ejecución
time.sleep(10)
# Cerramos la ventana
driver.close()
