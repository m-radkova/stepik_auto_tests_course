from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element(By.CSS_SELECTOR, "button[id=book]")

WebDriverWait(browser, 5).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"$100")
)
        
button.click()

x = browser.find_element(By.ID, "input_value").text #.text достаёт текст, который в тэге
res = calc(x)
browser.find_element(By.ID, "answer").send_keys(res)
browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


time.sleep(10)
browser.quit()