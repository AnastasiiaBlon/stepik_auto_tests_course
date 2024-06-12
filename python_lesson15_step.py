from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем браузер и переходим на страницу
link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Находим элементы, содержащие числа
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    # Получаем текст чисел и преобразуем их в целые числа
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Считаем сумму чисел
    sum_value = str(num1 + num2)

    # Находим выпадающий список и выбираем значение суммы
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_value)

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()