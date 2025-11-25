from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/math.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(300)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла