from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Создаем файл .txt
file_name = "empty.txt"
with open(file_name, "w") as file:
    file.write("")

# Открываем браузер и переходим на страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Заполняем текстовые поля
    first_name_input = browser.find_element(By.NAME, "firstname")
    first_name_input.send_keys("Ivan")
    
    last_name_input = browser.find_element(By.NAME, "lastname")
    last_name_input.send_keys("Petrov")
    
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("ivan.petrov@example.com")

    # Загрузка файла
    file_input = browser.find_element(By.ID, "file")
    file_path = os.path.join(os.getcwd(), file_name)
    file_input.send_keys(file_path)

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()
    # Удаляем созданный файл
    os.remove(file_name)