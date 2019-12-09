from selenium.webdriver.common.by import By



def test_enabled_button_to_cart(browser):
    """test to enabled button to add good in cart"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

    assert len(buttons) == 1
