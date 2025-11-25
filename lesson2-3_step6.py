import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем браузер
with webdriver.Chrome() as browser:
    # Открываем начальную страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    # Нажимаем на кнопку, которая открывает новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    
    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    
    # Решаем математическую задачу
    x = browser.find_element(By.ID, "input_value").text
    result = str(math.log(abs(12 * math.sin(int(x)))))
    
    # Вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(result)
    
    # Отправляем решение
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Копируем число из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    answer = alert.text.split()[-1]
    alert.accept()
    print(answer)