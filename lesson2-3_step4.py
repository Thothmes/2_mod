from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    # Открыть страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Принять alert
    alert = browser.switch_to.alert
    alert.accept()
    
    # Ждем загрузки новой страницы с капчей
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    
    # Решаем капчу быстро, пока не истекло время
    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text
    answer = calc(x_value)
    
    # Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer)
    
    # Нажимаем Submit (ждем, пока кнопка станет активной)
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
    )
    submit_button.click()
    
    # Получаем результат из alert
    result_alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    result_text = result_alert.text
    result_alert.accept()
    print("Ответ:", result_text)
    
finally:
    time.sleep(2)
    browser.quit()