from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Открываем страницу
with webdriver.Chrome() as driver:
    driver.get("https://SunInJuly.github.io/execute_script.html")
    
    # Считываем значение X
    x = int(driver.find_element(By.ID, "input_value").text)
    
    # Вычисляем математическую функцию
    result = math.log(abs(12 * math.sin(x)))
    
    # Прокручиваем страницу до текстового поля
    input_field = driver.find_element(By.ID, "answer")
    driver.execute_script("arguments[0].scrollIntoView(true);", input_field)
    
    # Вводим ответ
    input_field.send_keys(str(result))
    
    # Отмечаем checkbox
    checkbox = driver.find_element(By.ID, "robotCheckbox")
    driver.execute_script("arguments[0].click();", checkbox)
    
    # Выбираем radiobutton
    radio = driver.find_element(By.ID, "robotsRule")
    driver.execute_script("arguments[0].click();", radio)
    
    # Нажимаем кнопку Submit
    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].click();", button)
    
    # Получаем результат из alert
    time.sleep(1)
    alert = driver.switch_to.alert
    answer = alert.text
    alert.accept()
    print(answer)