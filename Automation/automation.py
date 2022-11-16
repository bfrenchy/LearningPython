from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# initiating webdriver and opening link
service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Show Message' in chrome_browser.page_source # ensuring we are on the right page

# input message
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
time.sleep(2)

# click to post message
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
time.sleep(2)

# check and print that the message was posted
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'My computer is typing for me' in output_message.text
print(output_message.text)

# exit driver
chrome_browser.quit()