from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click() 
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element(By.ID, "input_value").text #.text достаёт текст, который в тэге
    res = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.CSS_SELECTOR, "button[type = submit]").click()
    
finally:
     time.sleep(10)
     browser.quit()
   
   
    