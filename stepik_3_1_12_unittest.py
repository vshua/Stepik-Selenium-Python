from selenium import webdriver
import time
import unittest


class test_main(unittest.TestCase):
    def test_reg1(self):
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
            self.assertEqual("Congratulations! You have successfully registered!",
                             browser.find_element_by_tag_name('h1').text,
                             "Строка не совпала")
        finally:
            time.sleep(5)
            browser.quit()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
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
            self.assertEqual("Congratulations! You have successfully registered!",
                             browser.find_element_by_tag_name('h1').text,
                             "Строка не совпала")
        finally:
            time.sleep(5)
            browser.quit()


if __name__ == "__main__": unittest.main()
