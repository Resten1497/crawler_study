import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

driver = webdriver.Chrome('chromedriver.exe')
wb = openpyxl.Workbook()
ws = wb.active

def main():
    driver.get("https://www.musinsa.com/ranking/best")
    idx = 1
    ws.append(["id", "분류", "상품명", "가격", "좋아요수", "성별", "이미지url", "구매처 URL"])
    for i in range(5):
        type = driver.find_elements(By.XPATH, '//*[@id="goodsRankForm"]/div[1]/div[2]/dl/dd/ul/li')
        time.sleep(1)
        typeValue = type[i].text
        type[i].find_element(By.TAG_NAME,"a").send_keys(Keys.ENTER)
        for j in range(10):
            itemList = driver.find_element(By.ID,"goodsRankList").find_elements(By.CLASS_NAME,"li_box")
            brandName = itemList[j].find_element(By.CLASS_NAME,"item_title").text
            title = itemList[j].find_element(By.CLASS_NAME,"list_info").text
            price = itemList[j].find_element(By.CLASS_NAME,"price")
            likeCount = itemList[j].find_element(By.NAME,"count").text
            image = itemList[j].find_element(By.CLASS_NAME,"list_img").find_element(By.TAG_NAME,"img").get_attribute("data-original")
            url = itemList[j].find_element(By.CLASS_NAME, "list_img").find_element(By.TAG_NAME,"a").get_attribute("href")
            gender = itemList[j].find_element(By.CLASS_NAME,"icon_group").find_element(By.TAG_NAME,"ul").text


            try:
                original_price = price.find_element(By.TAG_NAME,"del")
                result = price.text.split(original_price.text)
                result_price = result[1].strip()
            except NoSuchElementException:
                result_price = price.text

            result = []
            result.append(idx)
            result.append(typeValue)
            result.append(title)
            result.append(result_price)
            result.append(likeCount)
            result.append(gender)
            result.append(image)
            result.append(url)
            print(result)
            ws.append(result)

            #print(brandName,"/",title,"/",result_price)
            idx +=1

    wb.save("musinsa.xlsx")


if __name__ == '__main__':
    main()