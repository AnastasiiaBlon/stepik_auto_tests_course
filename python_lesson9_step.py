from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    
    # Найти все поля ввода на странице
    elements = browser.find_elements(By.TAG_NAME, "input")
    
    # Заполнить каждое поле текстом "Мой ответ"
    for element in elements:
        element.send_keys("Мой ответ")
    
    # Найти и нажать кнопку отправки формы
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()