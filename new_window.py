from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    
    x = browser.find_element(By.ID, "input_value").text #.text достаёт текст, который в тэге
    res = calc(x)
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
finally:
    time.sleep(10)
    browser.quit()