from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from urllib.parse import urljoin, urlparse
import os
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    url = "https://www.pinterest.com/search/pins/?q=vtuber%20model"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10) # 如果没有sleep页面会立刻关闭，元素来不及读取
    images = driver.find_elements(By.XPATH, '//div[@data-test-id="pin-visual-wrapper"]//img')
    # div[@data-test-id="pin-visual-wrapper"]//img/@src
    # //div[@data-test-id="pin-visual-wrapper"]
    for img in images:
        src = img.get_attribute('src')
        src = src.replace('236x', 'originals')
        print(src)
    # print(images)
    # TODO: jiliguala
    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
