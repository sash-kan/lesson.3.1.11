from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    span = browser.find_element_by_css_selector("span#input_value")
    x = span.text

    answer = browser.find_element_by_css_selector("input#answer")
    answer.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_css_selector("input#robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
