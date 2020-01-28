import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS = '_1qNwV'
WHATSAPPWEB_MESSAGE_INPUT_CLASS = '_3u328'

options = webdriver.ChromeOptions()
options.binary_location = os.getenv('CHROMEPATH')
chrome_driver_binary = os.getenv('CRHOMEDRIVERPATH')
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get("http://web.whatsapp.com")

# Allow sign in
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS))
    )
except selenium.common.exceptions.TimeoutException:
    print("You didn't scan the code fast enough!")

# Locate correct contact
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
    print("Done!")

except selenium.common.exceptions.NoSuchElementException:
    print("Contact not found!")

driver.close()