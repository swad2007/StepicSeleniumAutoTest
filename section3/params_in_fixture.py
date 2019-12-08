import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By



# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1




@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    print(browser)
    text_area = browser.find_element(By.CLASS_NAME, "textarea")  #find_element_by_id("ember1599")
    text_area.send_keys(str(answer))
    button = browser.find_element(By.CLASS_NAME, "submit-submission")     #find_element_by_class("submit-submission")
    button.click()
    fidback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    print(fidback.text)
    assert "Correct!" in fidback.text

#The owls are not what they seem! OvO
