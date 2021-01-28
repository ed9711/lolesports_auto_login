import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username = ""
password = ""
browser = webdriver.Chrome()
browser.get("https://lolesports.com/")
browser.maximize_window()
login_button = browser.find_element_by_id("riotbar-account")
login_button.click()
username_field = browser.find_element_by_name("username")
username_field.send_keys(username)
password_field = browser.find_element_by_name("password")
password_field.send_keys(password)
submit_button = browser.find_element_by_class_name("mobile-button__submit")
submit_button.click()
