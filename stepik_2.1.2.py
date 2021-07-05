from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    time.sleep(1)
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    time.sleep(1)
    submit_btn = browser.find_element_by_css_selector(".btn.btn-default")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
	

