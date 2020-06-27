from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import app

xc = 0


def reset():
    global xc
    xc = 0

def scrap(search):
    global xc
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    # Here I am pressing the key combination to maximize the current window
    # Which alt+space+'x'
    # pyautogui.keyDown('alt')
    # pyautogui.press('space')
    # pyautogui.press('x')
    # pyautogui.keyUp('space')
    driver.get('https://www.youtube.com/results?search_query=' + search)
    # pyautogui.keyUp('alt')
    kosong = "              "
    # search = input('Search... ')

    # link = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div')
    # link.click()

    print('Pilih video')

    try:
        driver.execute_script("window.alert('Select the video you want to scrap.');")
        time.sleep(5)
        driver.switch_to_alert().accept()
    except NoAlertPresentException:
        print('He Clicked OK')

    for i in range(20, 0, -1):
        time.sleep(1)
        print('Countdown : ', end=" ")
        if (i < 10):
            print('0' + str(i), end="\r")
        else:
            print(i, end="\r")

    print('Done' + kosong)

    # driver.set_window_position(-2000,0)

    # actions = ActionChains(driver)
    # actions.key_down(Keys.ALT)
    # actions.key_down(Keys.SPACE)
    # actions.send_keys("n")
    # actions.perform()

    # Here I am pressing the key combination to minimize the current window
    # Which alt+space+'n'

    # driver.minimize_window()

    driver.execute_script('window.scrollTo(1, 500);')
    # pyautogui.keyDown('alt')
    # pyautogui.keyDown('space')
    # pyautogui.press('n')
    # pyautogui.keyUp('space')
    # pyautogui.keyUp('alt')
    # now wait let load the comments
    time.sleep(5)
    # driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[24]/div[2]/div[1]/span/button').click()

    index = 1
    # try:
    #     driver.execute_script("window.alert('Start Scraping Comments..');")
    #     time.sleep(5)
    #     driver.set_window_position(-2000, 0)
    # except UnexpectedAlertPresentException:
    #     driver.switch_to_alert().accept()
    #     driver.set_window_position(-2000, 0)
    # driver.switch_to_alert().accept()
    try:
        driver.execute_script("window.alert('Start Scraping Comments..');")
        time.sleep(5)
        driver.switch_to_alert().accept()
        # driver.set_window_position(-2000, 0)
    except NoAlertPresentException:
        # driver.set_window_position(-2000, 0)
        print('He Clicked OK')


    a = 'No'

    def commentSaved():
        comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
        comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
        return comments

   # get total comment per video
    x = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/h2/yt-formatted-string')
    v = filter(str.isdigit, x.text)
    z = []
    for i in v:
        z.append(i)

    z = ''.join(z)  # converting list into string
    z = int(z)
    print('TOTAL VIDEO COMMENTS :' + str(z))
    numberOfScrap = 500
    maxNumComment = 0
    index2 = 0
    index3 = 0

    while (a != 'Yes'):
        index1 = 0

        while (index1 < 3):  # Scroll sebanyak 5 kali
            # driver.execute_script('window.scrollTo(1, 400);')
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            # driver.execute_script('window.scrollTo(1, (document.body.scrollHeight)/2);')
            time.sleep(1.5)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1.5)
            index1 += 1
            temp = commentSaved()
            index2 = len(temp)

        print("Total Comments : " + str(index2))
        index3 += 1
        print(index3)

        if((index3%3) == 0): #Kalo hasil scrap 3 kali berturut2 sama
            if maxNumComment == index2:
                print('Breaking--')
                break
            else:
                print('Not Breaking---')
                maxNumComment = index2
        else:
            maxNumComment = index2

        if(index2>=z): #Kalo hasil scrap lebih besar dari total Comment
            xc = z
            a = 'Yes'
        else:
            if (index2 >= numberOfScrap): #kalo hasil scrap lebih besar dri 500
                xc = numberOfScrap
                a = 'Yes'
            else: #Kalo masih belum semua keambil/belum 500
                xc = index2

    #     #Nanya stop setiap 5 kali ngesave komen
    #     print("Total Comments : " + str(len(temp)))
    #     if((index%5) == 0):
    #         a = input('Stop? ')
    #     index += 1

    print("Udah")

    array = []
    comments = commentSaved()
    for comment in comments[:numberOfScrap]:
        array.append(comment.text)

    driver = driver.quit()

    return array

# scrap("Is Nokia Back?")

# from random import randint
# #
# # xc = 0
# #
# def RandInt():
#     global xc
#     xc += randint(0,100)
#
# #
# def vs():
#     return xc

# a = True
# while a:
#     RandInt()
#     print(xc)
#     print(vs())

#
# print(xc)