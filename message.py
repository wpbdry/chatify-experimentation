import os
import sys

from selenium import webdriver
import pickle

WHATSAPPWEB_MESSAGE_INPUT_CLASS = '_3u328'

if len(sys.argv) != 3:
    print("Please pass exactly three commant line parameters. File, contact name, and message.")
    exit()

options = webdriver.ChromeOptions()
options.binary_location = os.getenv('CHROMEPATH')
chrome_driver_binary = os.getenv('CRHOMEDRIVERPATH')
driver = webdriver.Chrome(chrome_driver_binary, options=options)
cookies = pickle.load(open('whatsapp_cookies.pkl', 'rb'))
print(len(cookies))
for cookie in cookies:
    print(cookie)
    driver.add_cookie(cookie)
driver.get('https://web.whatsapp.com')


print(sys.argv[0])
print(sys.argv[1])
