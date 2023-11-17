from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

warnings.filterwarnings("ignore")

URL_CURP = 'https://www.gob.mx/curp/'

def click_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def resolve_reCAPTCHA(driver):
    
    pass

def click_search_button(driver):
    # Espera hasta que el elemento obstructor desaparezca
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[style*='z-index: 2000000000']"))
    )
    
    search_button = driver.find_element(By.XPATH,"//*[@id='searchButton']")
    search_button.click()

def check_gender(driver):
    wait = WebDriverWait(driver, 20)
    gender_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember341"]/section/div[1]/div/div[2]/form/div[2]/div[1]/div/div[2]/table/tr[5]/td[2]')))
    gender = gender_element.text
    if gender == "MUJER":
        print("Es mujer.")
    elif gender == "HOMBRE":
        print("Es hombre.")
    else:
        print("No se pudo determinar el género.")

def main():
    #chrome_options = Options()
    #driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome()
    driver.get(URL_CURP)

    driver.implicitly_wait(10) # espera hasta 10 segundos antes de arrojar un error
    driver.find_element(By.XPATH, '//*[@id="curpinput"]').send_keys('POZD920419HDFRVV07')

    click_checkbox(driver)
    time.sleep(2)

    # Llamada a la función que resuelve el reCAPTCHA
    #resolve_reCAPTCHA(driver)

    click_search_button(driver)
    time.sleep(2)

    check_gender(driver)
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
