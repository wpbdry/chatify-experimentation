import os

import selenium
from selenium.webdriver.common.keys import Keys

import webdriver




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