import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_product(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector("button[type='submit']"), 'No button add to product'

