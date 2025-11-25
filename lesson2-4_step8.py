from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Ждем, пока цена не станет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    # Копируем результат из алерта
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    browser.quit()