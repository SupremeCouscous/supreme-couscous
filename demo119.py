from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

URL = "https://www.momoshop.com.tw/main/Main.jsp"
chrome = Chrome()
chrome.get(URL)
element = chrome.find_element(By.ID, "keyword")
element.clear()
element.send_keys("任天堂")
element.send_keys(Keys.RETURN)
time.sleep(5)
area = chrome.find_element(By.CLASS_NAME, "listArea")

products = area.find_elements(By.CLASS_NAME, "goodsUrl")
print(len(products))
for p in products:
    productName = p.find_element(By.CLASS_NAME, "prdName")
    print(productName.text)