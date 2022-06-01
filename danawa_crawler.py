from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')

def main():
    driver.get("https://www.danawa.com/")
    searchTag = driver.find_element(By.ID, "AKCSearch")
    searchTag.send_keys("RTX 3080")
    # GPU, RAM 만 검색 가능
    searchTag.send_keys(Keys.ENTER)
    pageNo = 1

    for i in range(pageNo, 4):
        print("PageNo : " + str(i))
        driver.execute_script("getPage(" + str(i) + ")")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
        for item in itemList:
            if item.get_attribute("id") != "":
                title = item.find_element(By.CLASS_NAME, "prod_name")
                priceitem = item.find_elements(By.CLASS_NAME, "top5_item")
                href = title.find_element(By.TAG_NAME,"a").get_attribute("href")
                #print(title.text)
                for price in priceitem:
                   print(title.text, " : ", price.text)



if __name__ == '__main__':
    main()