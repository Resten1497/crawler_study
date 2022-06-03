from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')

def main():
    wb = openpyxl.Workbook()
    ws = wb.active
    driver.get("https://www.danawa.com/")
    searchTag = driver.find_element(By.ID, "AKCSearch")
    searchTag.send_keys("RTX 3080")
    searchTag.send_keys(Keys.ENTER)
    pageNo = 1
    idx = 1
    ws.append(["id","상품명","가격","구매처 URL"])
    for i in range(pageNo, 3):
        print("PageNo : " + str(i))
        driver.execute_script("getPage(" + str(i) + ")")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
        for item in itemList:
            if item.get_attribute("id") != "":
                title = item.find_element(By.CLASS_NAME, "prod_name")
                priceitem = item.find_elements(By.CLASS_NAME, "top5_item")
                #href = title.find_element(By.TAG_NAME,"a").get_attribute("href")
                #print(href)
                title.find_element(By.TAG_NAME, "a").click()
                driver.switch_to.window(driver.window_handles[-1])
                title = driver.find_element(By.CLASS_NAME,"prod_tit")
                price = driver.find_element(By.CLASS_NAME,"lwst_prc")
                spec_list = driver.find_element(By.CLASS_NAME, "spec_list").text
                link = price.find_element(By.TAG_NAME,"a").get_attribute("href")
                #print(spec_list)
                print(title.text,price.text)
                ws.append([idx,title.text,price.text,link])
                idx = idx + 1
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(1)
        wb.save("danawa.xlsx")


if __name__ == '__main__':
    main()