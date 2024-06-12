import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функция для расчета значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер и переходим на страницу
link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Находим элемент, содержащий значение x, и считываем его
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Проскролливаем страницу вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Выбираем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Переключаем radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element(By.ID, "robotsRule")
    robots_rule_radiobutton.click()

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()