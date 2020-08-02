from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


# cчитать значение для переменной x
def calc(a, b):
    return (a + b)


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    b_element = browser.find_element_by_id("num2")
    a = int(a_element.text)
    b = int(b_element.text)
    sum = str(calc(a, b))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
