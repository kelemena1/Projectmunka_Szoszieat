from distutils.spawn import find_executable
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


bongeszo = webdriver.Chrome(executable_path=ChromeDriverManager().install())
bongeszo.get('http://127.0.0.1:5501/rolunk.html')
bongeszo.maximize_window()
bongeszo.save_screenshot("rolunkteteje.png")

time.sleep(1)
kapcsolat = bongeszo.find_element(By.XPATH,'//*[@id="navbarNavAltMarkup"]/div/a[1]')
kapcsolat.click()
bongeszo.maximize_window()
vezetek = "Kolompár"
Kereszt = "Sándor"
email = "valami@valami.hu"
uzenet = "valami nem jó xd\nxd"
vezetekmezo = bongeszo.find_element(By.XPATH,'//*[@id="firstname"]')
vezetekmezo.send_keys(vezetek)
time.sleep(1)
keresztmezo = bongeszo.find_element(By.XPATH,'//*[@id="lastname"]')
keresztmezo.send_keys(Kereszt)
time.sleep(1)
emailmezo = bongeszo.find_element(By.XPATH,'//*[@id="email"]')
emailmezo.send_keys(email)
time.sleep(1)
uzenetmezo = bongeszo.find_element(By.XPATH,'//*[@id="message"]')
uzenetmezo.send_keys(uzenet)
bongeszo.save_screenshot("kapcsolat.png")
gomb = bongeszo.find_element(By.XPATH,'//*[@id="kapcsolat"]/div/div[6]/input')
gomb.click()
time.sleep(2)
