from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем браузер и переходим на страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ожидание, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()
    
    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()