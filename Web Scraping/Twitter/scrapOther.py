from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def scrapOthers(listToScrap):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    final_retweet = []
    final_quote = []
    final_like = []
    count = 0

    for link in listToScrap:
        print(count)
        count += 1

        try:
            driver.get(link)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//article[@role="article"]')))
        except:
            final_retweet.append(0)
            final_quote.append(0)
            final_like.append(0)
            continue

        tempList = []
        numbers = driver.find_elements_by_xpath('//a[@role="link"]//span[@data-testid="app-text-transition-container"]')
        
        for i in numbers:
            tempList.append(i.text)

        listTitle = ['Retweet', 'Quote', 'Like']
        listFinal = []

        for j in listTitle:

            try:
                driver.find_element_by_xpath('//a[@role="link"]//span[contains(text(),"'+j+'")]')

                if '.' in tempList[0] :
                    tempList[0] = tempList[0].replace('K','00')
                else:
                    tempList[0] = tempList[0].replace('K','000')

                tempList[0] = tempList[0].replace(',','')
                tempList[0] = tempList[0].replace('.','')
                listFinal.append(int(tempList[0]))
                tempList.pop(0)
            except:
                listFinal.append(0)
                continue

        final_retweet.append(listFinal[0])
        final_quote.append(listFinal[1])
        final_like.append(listFinal[2])

    driver.quit()

    return final_retweet, final_quote, final_like

# listToScrap = ['google.com', 'https://twitter.com/iziiii25/status/1291242864903512064']
# listToScrap += ['https://twitter.com/bungsubungsut/status/1295672588459323392', 'https://twitter.com/BiLLRaY2019/status/1291707228102123522']
# print(scrapOthers(listToScrap))