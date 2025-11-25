from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Открываем страницу
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

# Считываем числа и вычисляем сумму
num1 = int(browser.find_element("id", "num1").text)
num2 = int(browser.find_element("id", "num2").text)
total = num1 + num2

# Выбираем значение в выпадающем списке
select = Select(browser.find_element("tag name", "select"))
select.select_by_value(str(total))  # Передаем строковое значение

# Нажимаем кнопку Submit
browser.find_element("css selector", "button.btn").click()

# Копируем число из алерта
alert = browser.switch_to.alert
answer = alert.text.split()[-1]
alert.accept()
print(answer)

# Закрываем браузер
browser.quit()