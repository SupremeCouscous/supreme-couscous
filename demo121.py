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
time.sleep(3)
area = chrome.find_element(By.CLASS_NAME, "listArea")

products = area.find_elements(By.CLASS_NAME, "goodsUrl")
print(len(products))
for p in products:
    print(p.get_property("href"))
    # print(p.get_attribute("innerHTML"))
    # print(p.text)
    productName = p.find_element(By.CSS_SELECTOR, ".prdImg.lazy.lazy-loaded")
    print(productName.get_attribute("title"))

products2 = area.find_elements(By.CLASS_NAME, "prdName")
for p in products2:
    print("***==>", p.text)

chrome.close()