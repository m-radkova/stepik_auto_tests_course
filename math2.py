from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    img = browser.find_element(By.ID, "treasure")
    x = int(img.get_attribute("valuex"))
    res = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type = submit]").click()
    
finally:
     time.sleep(10)
     browser.quit()