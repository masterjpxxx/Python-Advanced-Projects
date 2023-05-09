from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://portal.depedsdn.com/login?next=/')
email_address = ""
password = ""

email_input = browser.find_element(By.NAME,'username')
email_input.send_keys(email_address + Keys.RETURN)

password_input = browser.find_element(By.NAME,'password')
password_input.send_keys(password + Keys.RETURN)




