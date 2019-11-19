import math

from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    value = browser.find_element_by_id("input_value").text
    value1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", value1)
    value1.send_keys(calc(value))
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    check1 = browser.find_element_by_id("robotsRule")
    check1.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
