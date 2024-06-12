from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Найти все поля ввода на странице
    elements = browser.find_elements(By.TAG_NAME, "input")
    
    # Заполнить каждое поле текстом "Мой ответ"
    for element in elements:
        element.send_keys("Мой ответ")
    
    # Найти и нажать кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()