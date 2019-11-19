import math


from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

value1 = browser.find_element_by_id("num1")
value2 = browser.find_element_by_id("num2")

select1 = Select(browser.find_element_by_id("dropdown"))
select1.select_by_value(str(int(value1.text)+int(value2.text)))

buttonSub = browser.find_element_by_class_name("btn")
buttonSub.click()
