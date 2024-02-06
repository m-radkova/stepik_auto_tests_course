from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    
    res = num1 + num2 
    
    select1 = Select(browser.find_element(By.ID, "dropdown"))
    select1.select_by_value(str(res))
    
    browser.find_element(By.CSS_SELECTOR, "button[type = submit]").click()
   

finally:
     time.sleep(10)
     browser.quit()