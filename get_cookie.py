import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")

all_cookie = driver.get_cookies()

print(all_cookie)

driver.close()