from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element_by_id("#answer.form-control")
    answer.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element_by_id("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("#robotsRule")
    option2.click()
    submit_btn = browser.find_element_by_css_selector(".btn.btn-default")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
	

