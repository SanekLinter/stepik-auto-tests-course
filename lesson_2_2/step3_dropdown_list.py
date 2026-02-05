from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    answer = calc(num1.text, num2.text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
