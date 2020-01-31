import os
import sys
import logging

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle

WHATSAPPWEB_MESSAGE_INPUT_CLASS = '_3u328'
logging.basicConfig(level=logging.INFO)

options = webdriver.ChromeOptions()
options.binary_location = os.getenv('CHROMEPATH')
# options.add_argument('headless')
# options.add_argument('window-size=12000x6000')
chrome_driver_binary = os.getenv('CRHOMEDRIVERPATH')
driver = webdriver.Chrome(chrome_driver_binary, options=options)

# Log in
logging.info("Logging you in...")
driver.get('https://web.whatsapp.com')
logging.debug("get complete")
local_storage = pickle.load(open('whatsapp_lstorage.pkl', 'rb'))
logging.debug(len(local_storage))
for k, v in local_storage.items():
    logging.debug(k, v)
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", k, v)
logging.debug("copying local storage complete")
driver.get('https://web.whatsapp.com')
logging.debug("second get complete")

try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, 'input'))
    )
except selenium.common.exceptions.TimeoutException:
    logging.error("timeout")
    exit()
logging.info("Ready!")

# Send messages
while True:
    contact_name = input('Who would you like to message (name)?: ')
    search_bar = driver.find_element_by_tag_name('input')
    search_bar.send_keys(contact_name)
    search_bar.send_keys(Keys.RETURN)
    try:
        message_input = driver.find_element_by_class_name(WHATSAPPWEB_MESSAGE_INPUT_CLASS)

        # Send  message
        message = input("Message: ")
        message_input = driver.find_element_by_class_name(WHATSAPPWEB_MESSAGE_INPUT_CLASS)
        message_input.send_keys(message)
        message_input.send_keys(Keys.RETURN)
        logging.info("Message sent!")

    except selenium.common.exceptions.NoSuchElementException:
        logging.info("Contact not found!")

