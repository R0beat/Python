from selenium import webdriver # Modulo que provee todas las implementaciones
import time # Se usa para agregar demora en la ejecución de un programa
# Importamos
from webdriver_manager.chrome import ChromeDriverManager 
# Usamos el controlador para que se se ejecute o instale
driver = webdriver.Chrome(ChromeDriverManager().install())
# Abre la pagina que deseamos visitar y el tiempo de ejecución
# Teléfono
celular = "*********"
# Mensaje
mensaje = "XXXXXXX XXXXXXXXXXX XXXXXXXXXX XXXXXXXXXX"
# Concatenamos el celular y elmensaje a la ulr de la API de WhatsApp
driver.get("https://wa.me/52"+celular+'?text='+mensaje)
# Definimos el tiempo de ejecución
time.sleep(5)
# Encontramos el XPath del elemento HTML
btn = driver.find_elements_by_xpath('//*[@id="action-button"]')[0]
btn.click()
time.sleep(5)

btn = driver.find_elements_by_xpath('//*[@id="fallback_block"]/div/div/a')[0]
btn.click()
time.sleep(5)
# Boton Enviar
btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(5)
# Fin del Boot
print("-- Fin de Bot--")
# Timer
time.sleep(40)
# Cerramos el Navegador
driver.close()
