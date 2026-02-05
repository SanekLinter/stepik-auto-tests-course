from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Alexander")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Bratenkov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("somemail@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
