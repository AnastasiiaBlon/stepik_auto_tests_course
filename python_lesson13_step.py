import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# URL страницы
link = "https://suninjuly.github.io/math.html"

try:
    # Открываем браузер и переходим на страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()