from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/execute_script.html'

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x = int(browser.find_element(By.ID, "input_value").text)
    res = calc(x)
    browser.find_element(By.ID, "answer").send_keys(res)
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   
    
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    
    
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()