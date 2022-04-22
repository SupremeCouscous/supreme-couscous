from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "https://www.momoshop.com.tw/main/Main.jsp"
chrome = Chrome()
chrome.get(URL)
element = chrome.find_element(By.ID, "keyword")
element.clear()
element.send_keys("任天堂")
element.send_keys(Keys.RETURN)

# time.sleep(3)
# area = chrome.find_element(By.CLASS_NAME, "listArea")
# get listArea <-- not empty listArea
area = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "listArea")))
# make sure at least 1 goodsUrl will show
aProduct = WebDriverWait(area, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "goodsUrl")))
#
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
