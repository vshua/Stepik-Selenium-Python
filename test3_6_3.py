from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_correct_answer(browser,links):
    link = f"{links}"
    browser.get(link)
    browser.implicitly_wait(5)
    enter_number = browser.find_element_by_css_selector(".ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer = str(math.log(int(time.time())))
    enter_number.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    assert browser.find_element_by_css_selector(".smart-hints__hint").text == "Correct!"




