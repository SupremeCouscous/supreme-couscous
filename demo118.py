from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome = Chrome()
chrome.get("https://shopping.pchome.com.tw/")
element = chrome.find_element(By.ID, "keyword")
element.clear()
element.send_keys("任天堂")
element.send_keys(Keys.RETURN)