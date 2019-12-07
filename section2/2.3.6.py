from selenium import webdriver
import math


link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    main_button = browser.find_element_by_class_name("trollface")
    main_button.click()
    browser.switch_to.window(browser.window_handles[1])
    input_value = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(int(input_value.text)))
    second_button = browser.find_element_by_class_name("btn-primary")
    second_button.click()

except Exception as e:
    print(e)
finally:
    browser.close()
