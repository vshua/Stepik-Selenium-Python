from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_css_selector(".nowrap#num1")
    num1 = number1.text  # attribute "text"
    n1 = int(num1)
    number2 = browser.find_element_by_css_selector(".nowrap#num2")
    num2 = number2.text
    n2 = int(num2)
    y = n1 + n2
    summ_y = str(y)
    select = Select(browser.find_element_by_tag_name(".custom-select"))
    select.select_by_visible_text(summ_y)
    submit_btn = browser.find_element_by_css_selector(".btn.btn-default")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
	

