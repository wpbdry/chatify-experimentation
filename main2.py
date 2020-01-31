import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

def save_local_storage():
    local_storage_values = driver.execute_script( \
                "var ls = window.localStorage, items = {}; " \
                "for (var i = 0, k; i < ls.length; ++i) " \
                "  items[k = ls.key(i)] = ls.getItem(k); " \
                "return items; ")

    dumpedStorage = json.dumps(local_storage_values)
    f = open("localStorageSavedValues.json","w")
    f.write(dumpedStorage)
    f.close()

def check_for_local_storage_file():
    return os.path.exists('localStorageSavedValues.json')

def inject_local_storage_data_to_browser():
    with open('localStorageSavedValues.json', 'r') as f:
        parsed_local_storage_json = json.load(f)
    
    for key, value in parsed_local_storage_json.items():
        driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS = '_1qNwV'
WHATSAPPWEB_MESSAGE_INPUT_CLASS = '_3u328'

# options = webdriver.ChromeOptions()
# options.binary_location = os.getenv('CHROMEPATH')
# chrome_driver_binary = os.getenv('CRHOMEDRIVERPATH')
# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com")

if check_for_local_storage_file():
    inject_local_storage_data_to_browser()    
    driver.get("http://web.whatsapp.com")
    save_local_storage()

# Allow sign in

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, WHATSAPPWEB_EMPTY_CHAT_PANE_CLASS))
    )
except selenium.common.exceptions.TimeoutException:
    print("You didn't scan the code fast enough!")

save_local_storage()

# Locate correct contact

def locate_correct_contact():
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
    locate_correct_contact()

locate_correct_contact()

# driver.close()
