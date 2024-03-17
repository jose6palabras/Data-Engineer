from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/josel/.config/chromium/Default")

driver = webdriver.Chrome(executable_path=r'/home/josel/Descargas/chromedriver', chrome_options=options) 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
user = ['"JoseLuis"', '"FabioZapata"', '"Familia SECTOR BUENOS AIRES 55"', '"Familia SECTOR GRANJA 110"']

for i in range(0, len(user)):
	# Replace the below string with your own message 
	string = user[i] + " " +"estoy probando" + " " + "ultima prueba de hoy con usted jajaja"
	x_arg = '//span[contains(@title,' + user[i] + ')]'
	group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
	group_title.click() 
	inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
	input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(2) 


