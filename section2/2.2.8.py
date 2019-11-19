from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

value = browser.find_element(By.NAME, "firstname")
value.send_keys("test")
value1 = browser.find_element(By.NAME, "lastname")
value1.send_keys("test")
value2 = browser.find_element(By.NAME, "email")
value2.send_keys("test")
value3 = browser.find_element_by_css_selector("[type=file]")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
value3.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
