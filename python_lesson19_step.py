from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем браузер и переходим на страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()
    
    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Ждем загрузки новой страницы
    time.sleep(1)
    
    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()