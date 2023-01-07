from selenium.webdriver.common.by import By
import time
from selenium import webdriver 
from sys import argv

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements(By.CSS_SELECTOR, '[required]') 
    for el in elements: 
        el.send_keys('sample input')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
