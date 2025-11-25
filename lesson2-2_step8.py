import tempfile
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем временный текстовый файл
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_file:
    tmp_file.path = tmp_file.name

driver = webdriver.Chrome()
try:
    # Открываем страницу
    driver.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    driver.find_element(By.NAME, "firstname").send_keys("Иван")
    driver.find_element(By.NAME, "lastname").send_keys("Петров")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Загружаем файл
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(tmp_file.path)
    
    # Нажимаем кнопку отправки
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Копируем число из алерта
    alert_text = driver.switch_to.alert.text
    answer = alert_text.split()[-1]  # Извлекаем число из текста алерта
    print("Результат:", answer)
finally:
    driver.quit()
    os.unlink(tmp_file.path)  # Удаляем временный файл