from selenium.webdriver.common.by import By
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    # elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    #OR
    # elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']") 
    #OR
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element(
        By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
