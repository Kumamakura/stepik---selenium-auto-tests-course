from selenium import webdriver
import time
import math


# cчитать значение для переменной x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x_element = browser.find_element_by_id("treasure")
    value = x_element.get_attribute("valuex")
    y = calc(value)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    time.sleep(1)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
