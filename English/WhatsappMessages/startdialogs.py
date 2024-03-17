#!/usr/bin/python
# -*- coding: utf8 -*-
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import pandas as pd
#toma bd de contactos
data = pd.read_csv('WhatsApp_contacts_verified.csv', usecols=['Display Name'], encoding='utf-8')
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/josel/.config/chromium/Default")

driver = webdriver.Chrome(executable_path=r'/home/josel/Documentos/Detec/BigData/interes_comun/chromedriver', chrome_options=options) 
#abre la ventana de Google Crhome
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600)
f = open ("conteo_soporte.txt", "w")

for i in range(542, len(data)):
    x_arg_chat = '//html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg_chat)))
    group_title.click()
    search = driver.find_elements_by_class_name('eiCXe')
    time.sleep(1)
    search[0].send_keys("Jose Ribero")
    time.sleep(1)
    search[0].send_keys(Keys.ENTER)
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    #envia el mensaje deseado
    input_box.send_keys(u"Hola, soy Memo Gómez y cuento contigo para que juntos construyamos el camino de desarrollo que necesita Cocorná. Te invito a que conozcas más de mí, viendo este video:  https://cutt.ly/Eovg61")
    time.sleep(5)
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys(u"¿Cuéntanos qué opinas? \n")
    attache = driver.find_elements_by_ccs_selector('.GPmgf > div:nth-child(1) > span:nth-child(1)')       
    f.write(str(i)+ "\n")
    time.sleep(1)
f.close()



