from selenium import webdriver
import time
import unittest


class TestSMF(unittest.TestCase):


    def registration_helper(self, link):

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        value = browser.find_element_by_class_name("first_block").find_element_by_class_name("first")
        value.send_keys("value1")

        value2 = browser.find_element_by_class_name("first_block").find_element_by_class_name("second")
        value2.send_keys("value2")

        value3 = browser.find_element_by_class_name("first_block").find_element_by_class_name("third")
        value3.send_keys("value3")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


        browser.quit()


    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"

        self.registration_helper(link)



    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        self.registration_helper(link)

if __name__ == "__main__":
    unittest.main()
