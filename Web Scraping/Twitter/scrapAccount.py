from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def tesNewTab():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.google.com/search?q=python&source=hp&ei=d2laYo7mJZiq4t4P2-i5oAI&iflsig=AHkkrS4AAAAAYlp3hyyavh4A6-YzyCQXupH2wo5lBhmr&ved=0ahUKEwjO_bWegZj3AhUYldgFHVt0DiQQ4dUDCAc&uact=5&oq=python&gs_lcp=Cgdnd3Mtd2l6EANQAFgAYGxoAHAAeACAAQCIAQCSAQCYAQDAAQE&sclient=gws-wiz')
    first_result = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('yuRUbf'))
    first_link = first_result.find_element_by_tag_name('a')

    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = driver.current_window_handle

    # Open the link in a new tab by sending key strokes on the element
    # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
    first_link.send_keys(Keys.CONTROL + Keys.RETURN)
    
    windows = driver.window_handles

    for w in windows:
    #switch focus to child window
        if(w!=main_window):
            driver.switch_to.window(w)
            break

    # do whatever you have to do on this page, we will just got to sleep for now
    time.sleep(10)
    print("Child window title: " + driver.title)

    # Close current tab
    driver.close()

    # Put focus on current window which will be the window opener
    driver.switch_to.window(main_window)
    print("Child window title: " + driver.title)
    time.sleep(10)
    print(aufar)

def scrapOthers(listToScrap):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('https://twitter.com/adele')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//article[@role="article"]')))
    links = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')

    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = driver.current_window_handle


    for i in links:
        # Open the link in a new tab by sending key strokes on the element
        # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
        i.send_keys(Keys.CONTROL + Keys.RETURN)
        
        windows = driver.window_handles

        for w in windows:
        #switch focus to child window
            if(w!=main_window):
                driver.switch_to.window(w)
                break

        # do whatever you have to do on this page, we will just got to sleep for now
        time.sleep(2)
        print("Child window title: " + driver.title)

        # Close current tab
        driver.close()

        # Put focus on current window which will be the window opener
        driver.switch_to.window(main_window)
        print("Child window title: " + driver.title)
        time.sleep(2)
        print("===================")


def getSpecificAccountData(listToScrap):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://twitter.com/i/flow/login')

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input')))

    driver.find_element_by_xpath('//input').send_keys('@AyuhmDyah')
    driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))

    driver.find_element_by_xpath("//input[@type='password']").send_keys('dyahayuhm26')
    driver.find_element_by_xpath('//span[contains(text(),"Log")]').click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"happening")]')))

    for i in listToScrap:
        driver.get(i)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//article[@role="article"]')))
        driver.find_element_by_xpath('//span[contains(text(),"Suka")]').click()
        time.sleep(2)
        liElement = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div')
        for j in range(999999999):
            driver.execute_script("arguments[0].scrollIntoView(true);", liElement)
        
        time.sleep(10000000)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        # links = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')

    time.sleep(10000000)

    # //input
    # //span[contains(text(),"Next")]
    # //input[@type='password']
    #  //span[contains(text(),"Log")]


listToScrap = ['https://twitter.com/convomfs/status/1493821270534008832', 'https://twitter.com/WidyoLita/status/1288676171861770242']
listToScrap += ['https://twitter.com/yusril_kurzah/status/1288709928752824320', 'https://twitter.com/remukanbakwan__/status/1288845902422056961']
listToScrap += ['https://twitter.com/nksthi/status/1288638758821040128', 'https://twitter.com/panjidorky13/status/1289050938607407107']
listToScrap += ['https://twitter.com/Felizersyhy/status/1288660407817629696', 'https://twitter.com/kholidpurnomoaj/status/1288854395359174659']
print(getSpecificAccountData(listToScrap))

# Core :
# //article[@role="article"]
 
# If :
# div[contains(text(),"Replying")]

# Childs :
# //span[@class='css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0']
# //span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" and contains(text(),'@') and not(contains(text(),'@Adele'))]
# //time
# //span[contains(text(),'Show more replies')]
# ActionChains(driver).move_to_element(element).perform()
