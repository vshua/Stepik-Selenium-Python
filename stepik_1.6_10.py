from selenium import webdriver
import time
try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector(":required.form-control.first")
    input1.send_keys("I")
    input2 = browser.find_element_by_css_selector(":required.form-control.second")
    input2.send_keys("P")
    input3 = browser.find_element_by_css_selector(":required.form-control.third")
    input3.send_keys("Kyiv@gmail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name('h1').text
finally:
    time.sleep(5)
    browser.quit()

