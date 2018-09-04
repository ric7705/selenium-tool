from selenium import webdriver

from selenium.webdriver.firefox.options import Options

# # chrome
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=options)
#
# driver.get("http://www.python.org")
# all_cookie = driver.get_cookies()
# print(all_cookie)



# firefox
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

driver.get("http://www.python.org")
all_cookie = driver.get_cookies()
print(all_cookie)