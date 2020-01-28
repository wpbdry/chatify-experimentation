import os

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle

WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS = '_1qNwV'

options = webdriver.ChromeOptions()
options.binary_location = os.getenv('CHROMEPATH')
chrome_driver_binary = os.getenv('CRHOMEDRIVERPATH')
driver = webdriver.Chrome(chrome_driver_binary, options=options)
driver.get('https://web.whatsapp.com')
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS))
    )
    driver.implicitly_wait(2)
    cookies = driver.get_cookies()
    print(len(cookies))  # Why is this printing 0??
    pickle.dump(cookies, open('whatsapp_cookies.pkl','wb'))
    # driver.quit()
except selenium.common.exceptions.TimeoutException:
    print("You didn't scan the code fast enough!")
