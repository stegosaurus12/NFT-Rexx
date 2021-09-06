#!/usr/bin/python3

import os
import time
import re
import random
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get file path
dirname = os.path.dirname(os.path.abspath(__file__))
imgpath = dirname + "/image_output/"
filename = dirname + "/all_feature_list_numerical_order.txt"

# create empty dictionary for features
nfts = defaultdict(defaultdict)

# open file and read in all lines up to numlines
count = 0
# file number to start reading in (file #0 = 0)
filestart = 1
numlines = 5
print("Starting at NFT #" + str(filestart))
print("Uploading " + str(numlines) + " NFTs\n")
numlines1 = numlines
with open(filename) as features:
    for line in features:
        (file, name, eye, head, butt, mouth, hand, flip,
         upsidedown) = line.split("\t")
        if name == "Name":
            continue
        if count >= filestart:
            nfts[name]['eye'] = eye
            nfts[name]['head'] = head
            nfts[name]['butt'] = butt
            nfts[name]['mouth'] = mouth
            nfts[name]['flip'] = flip
            nfts[name]['hand'] = hand
            nfts[name]['upsidedown'] = upsidedown
            nfts[name]['file'] = file
            numlines -= 1
        count += 1
        if numlines <= 0:
            break

print("First few files:")
if numlines1 < 10:
    first_few = numlines1
else:
    first_few = 10

for counter, key in enumerate(nfts):
    if counter < first_few:
        print(key)
    else:
        break
print()


temp_pw = 'temporarypw69'
seed = 'seed phrase here'  ###CAREFUL NOT TO SHARE THIS!

# open up chrome with metamask, need to get crx extension for MM first
METAMASK_PATH = 'path to MM .crx file'
opt = webdriver.ChromeOptions()
opt.add_extension(METAMASK_PATH)
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=opt)

# navigate metamask and log into account
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_tag_name('body').send_keys(Keys.TAB + Keys.ENTER + Keys.TAB + Keys.ENTER + Keys.TAB + Keys.ENTER) 
#driver.find_elements_by_xpath('//input')
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.TAB + Keys.TAB + seed + Keys.TAB + Keys.TAB + temp_pw + Keys.TAB + temp_pw + Keys.TAB + Keys.SPACE + Keys.TAB + Keys.TAB + Keys.ENTER + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

'''
# pause to make sure metamask is ok
temp = input("Make sure metamask is finished. Type 'y' to continue\n")
if temp == 'y':
    print("hooray!")
else:
    print("closing now...")
    driver.quit()
    quit()
'''

# navigate to opensea
driver.switch_to.window(driver.window_handles[1])
driver.get("opensea url")

# load metamask
driver.find_element_by_xpath('//i[@value="account_balance_wallet"]').click()
try:
    mm_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="MetaMask"]')))
except:
    print("Can't load MetaMask button! Quitting!")
    #driver.quit()
    #quit()
mm_button.click()
# make sure to wait until metamask prompt loads
for i in range(120):
    num_window_handles1 = len(driver.window_handles)
    if num_window_handles1 < 3:
        time.sleep(1)
        continue
    elif num_window_handles1 == 3:
        break
    else:
        print("Something is wrong with the program! Line 124! Quitting!")
        driver.quit()
        quit()
'''
driver.switch_to.window(driver.window_handles[num_window_handles1 - 1])
time.sleep(5)
try:
    next_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Next"]')))
except:
    print("Can't load next button! Quitting!")
    #driver.quit()
    #quit()
time.sleep(1)
next_button.click()
driver.find_element_by_xpath('//button[text()="Connect"]').click()
time.sleep(5)
if len(driver.window_handles) == 3:
    driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
'''

# pause to make sure connected to metamask

temp = input("Connect to metamask. Type 'y' to continue\n")
if temp == 'y':
    print("hooray!")
else:
    print("closing now...")
    driver.quit()
    quit()


driver.get("opensea url")

PAUSE = True # pause first time through loop to verify metamask
start_time = time.time()

# start loop here to upload and list NFTs
for key in nfts:
    print("Starting:", key)
    driver.find_element_by_partial_link_text("Add item").click()

    if PAUSE:
        #input('Press any button to continue once finished with metamask')
        PAUSE = False
        for i in range(120):
            num_window_handles2 = len(driver.window_handles)
            if num_window_handles2 < 3:
                time.sleep(1)
                continue
            elif num_window_handles2 == 3:
                break
            else:
                print("Something is wrong with the program! Line 171! Quitting!")
                driver.quit()
                quit()
        driver.switch_to.window(driver.window_handles[num_window_handles1 - 1])
        try:
            sign_button2 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//button[text()="Sign"]')))
        except:
            print("Can't load initial sign button! Quitting!")
            driver.quit()
            quit()
        sign_button2.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
    else:
        pass

    imgfile = imgpath + nfts[key]['file']
    try:
        media_file = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'media')))
    except:
        print("Can't load media upload window! Quitting!")
        driver.quit()
        quit()
    media_file.send_keys(imgfile)
    driver.find_element_by_id('name').send_keys(key)
    driver.find_element_by_id('description').send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

# fill out properties
    for i in range(6):
        driver.find_element_by_xpath('//button[text()="Add more"]').click()
    eye_prop =  nfts[key]['eye']
    head_prop = nfts[key]['head']
    butt_prop = nfts[key]['butt']
    mouth_prop = nfts[key]['mouth']
    hand_prop = nfts[key]['hand']
    flip_prop = str(nfts[key]['flip']).lower()
    upsidedown_prop = str(nfts[key]['upsidedown']).lower().rstrip()
    all_props = "eye" + Keys.TAB + eye_prop + Keys.TAB + "head" + Keys.TAB + head_prop + Keys.TAB + "mouth" + Keys.TAB + mouth_prop + Keys.TAB + "butt" + Keys.TAB + butt_prop + Keys.TAB + "hand" + Keys.TAB + hand_prop + Keys.TAB + "flip" + Keys.TAB + flip_prop + Keys.TAB + "upsidedown" + Keys.TAB + upsidedown_prop
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB + all_props)
    driver.find_element_by_xpath('//button[text()="Save"]').click()

# decide what blockchain to mint on
    chain = None
    chain = random.choices(["Ethereum", "Polygon"], weights = [70, 30], k = 1)[0]
    print(chain)
    if chain == "Ethereum":
        pass
    else:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_elements_by_xpath('//i[@value="keyboard_arrow_down"]')[1].click()
        driver.find_element_by_xpath('//*[contains(@id,"tippy")]').click()

# mint nft
    driver.find_element_by_xpath('//button[text()="Create"]').click()
    try:
        temp_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//i[@value="link"]')))
    except:
        print("Can't load NFT created window! Quitting!")
        driver.quit()
        quit()
    time.sleep(0.5)
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

# set price
    price = 0.01

# put up for sale
    if chain == "Ethereum":
        try:
            sell_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Sell"]')))
        except:
            try:
                driver.refresh()
                sell_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Sell"]')))
            except:
                print("Can't find sell button! Quitting!")
                driver.quit()
                quit()
#       driver.find_element_by_xpath('//a[text()="Sell"]').click()
        sell_button.click()
        try:
            learn_more_link = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Learn more.')))
        except:
            print("Can't load sale page! Quitting!")
            driver.quit()
            quit()
        driver.find_elements_by_xpath('//input')[1].send_keys(str(price))
        driver.find_element_by_xpath('//button[text()="Post your listing"]').click()
# make sure to wait until metamask prompt loads
        for i in range(120):
            num_window_handles = len(driver.window_handles)
            if num_window_handles < 3:
                time.sleep(1)
                continue
            elif num_window_handles == 3:
                break
            else:
                print("Something is wrong with the program! Line 308! Quitting!")
                driver.quit()
                quit()
        driver.switch_to.window(driver.window_handles[num_window_handles - 1])
        try:
            sign_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//button[text()="Sign"]')))
        except:
            print("Can't load sign button! Quitting!")
            driver.quit()
            quit()
        sign_button.click()
    #driver.find_element_by_xpath('//button[text()="Sign"]').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    elif chain == "Polygon":
        try:
            sell_button2 = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Sell"]')))
        except:
            try:
                driver.refresh()
                sell_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Sell"]')))
            except:
                print("Can't find sell button! Quitting!")
                #driver.quit()
                quit()
#       driver.find_element_by_xpath('//a[text()="Sell"]').click()
        sell_button2.click()
        driver.implicitly_wait(5)
        try:
            price_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Amount"]')))
        except:
            print("Can't load sale page! Quitting!")
#            #driver.quit()
            quit()
        price_input.send_keys(str(price))
#        driver.implicitly_wait(5)
#        WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//input[@placeholder='Amount']")).send_keys(str(price))
        driver.find_element_by_xpath('//button[text()="Complete listing"]').click()
# ???may need to sign? every time or just once? looks like every time
        try:
            sign_button3 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign"]')))
        except:
            print("Can't load sale page! Quitting!")
            #driver.quit()
            quit()
        sign_button3.click()
    # make sure to wait until metamask prompt loads
        for i in range(120):
            num_window_handles3 = len(driver.window_handles)
            if num_window_handles3 < 3:
                time.sleep(1)
                continue
            elif num_window_handles3 == 3:
                break
            else:
                print("Something is wrong with the program! Line 124! Quitting!")
                driver.quit()
                quit()
        driver.switch_to.window(driver.window_handles[num_window_handles3 - 1])
        try:
            sign_button4 = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign"]')))
        except:
            print("Can't load Sign button! Quitting!")
            driver.quit()
            quit()
        sign_button4.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
    else:
        print("Something is wrong with chain output! Quitting!")
        driver.quit()
        quit()


# navigate back to starting page and loop through again
    time.sleep(0.5)
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    driver.get("opensea url")
    print("Finished:", key)

total_time = time.time() - start_time
print("Done!")
print("Total time:", round(total_time, 3), "sec", "=", round(total_time/60, 3), "min")
print("Avg time per NFT:", round(total_time/numlines1, 3), "sec")
