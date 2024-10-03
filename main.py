from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    query = "vtuber model"
    url = "https://www.pinterest.com/search/pins/?q=" + query
    img_set = set()
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)  # 如果没有sleep页面会立刻关闭，元素来不及读取
    limit = 5  # 滑动5次可以下载18张图片
    for i in range(limit):
        images = driver.find_elements(By.XPATH, '//div[@data-test-id="pin-visual-wrapper"]//img')
        # div[@data-test-id="pin-visual-wrapper"]//img/@src
        # //div[@data-test-id="pin-visual-wrapper"]
        for img in images:
            src = img.get_attribute('src')
            src = src.replace('236x', 'originals')
            img_set.add(src)
        driver.execute_script('window.scrollBy(0, window.innerHeight);')
    filename = f"{query}.txt"
    with open(filename, "w") as file:
        for elem in img_set:
            print(elem)
            file.write(elem + "\n")

    print("size:", len(img_set))
    # print(images)


if __name__ == '__main__':
    main()
