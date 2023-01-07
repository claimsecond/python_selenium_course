from selenium.webdriver.common.by import By
import time
from selenium import webdriver 
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn.click()

finally:
   
    time.sleep(10)
    browser.quit()


