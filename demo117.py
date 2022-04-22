from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time

chrome = Chrome()
chrome.get("https://www.python.org")
# queryField = chrome.find_element_by_name("q")
#queryField = chrome.find_element(By.NAME, "q")
#queryField = chrome.find_element(By.ID, "id-search-field")
queryField = chrome.find_element(By.CSS_SELECTOR, "input#id-search-field.search-field")
queryField.clear()
queryField.send_keys("developer")
queryField.send_keys(Keys.RETURN)
time.sleep(5)
chrome.close()