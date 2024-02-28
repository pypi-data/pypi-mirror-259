import random
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
import shutil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pyautogui
import re
from cross_border_mover import driver1
import win32gui, win32com.client
# https://detail.1688.com/offer/763190942317.html?spm=a26352.13672862.offerlist.10.5b7b1e62luVLRY
def getSKUInfo(url):

    driver = driver1.getDriver()
    driver.get(url)
    driver1.setToTop(driver)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(0.2, 1.2))
    # driver.execute_script("window.scrollBy(0,500)　")
    # time.sleep(1)
    try:
        detailElm = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"od-pc-layout-detail-tab-container")))
    except:
        print("hwnd===========no")
        
    driver.execute_script("arguments[0].scrollIntoView();",detailElm)
    time.sleep(random.uniform(0.2, 1.2))
    h = random.uniform(500, 1000)
    driver.execute_script("window.scrollBy(0,-500)".format(h))
    time.sleep(random.uniform(0.2, 1.2))
    actions = ActionChains(driver)
    try:
        sku_expend = driver.find_element(By.CLASS_NAME,"sku-wrapper-expend-button")
        
        actions.move_to_element(sku_expend)
        actions.click(sku_expend)
        actions.perform()
    except:
        print('no sku_expend button')

    
    colorList = []
    sku_items = driver.find_elements(By.CLASS_NAME,"prop-item")
    # print(sku_items)
    for skus_item in sku_items:
        styleStr = 'no img'
        try:
          styleStr = skus_item.find_element(By.CLASS_NAME,"prop-img").get_attribute("style")
        except:
            print("NO image")
            
        url = 'no img url'
        if styleStr != 'no img':
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', styleStr)
            if type(urls) == list:
                url = urls[0]
        title = skus_item.find_element(By.CLASS_NAME,"prop-name").text
        # print(title , url)
        colorList.append({"title":title,"url":url})    
    # print(colorList)
    
    sku_sizes = driver.find_elements(By.CLASS_NAME,"sku-item-wrapper")
    
    sizeList = []
    for sku_size in sku_sizes:
        size_text = sku_size.find_element(By.CLASS_NAME,"sku-item-name").text
        sizeList.append(size_text)
        
    # print(sizeList)
    # driver.quit()

    return colorList,sizeList


# https://detail.1688.com/offer/715593582127.html
def getColorInfo(url):
    driver = driver1.getDriver()
    driver.get(url)
    driver1.setToTop(driver)

        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(0.2, 1.2))
    # driver.execute_script("window.scrollBy(0,500)　")
    # time.sleep(1)
    try:
        detailElm = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"od-pc-layout-detail-tab-container")))
    except:
        print("hwnd===========no")
    driver.execute_script("arguments[0].scrollIntoView();",detailElm)
    time.sleep(random.uniform(0.2, 1.2))
    h = random.uniform(500, 1000)
    driver.execute_script("window.scrollBy(0,-500)".format(h))
    time.sleep(random.uniform(0.2, 1.2))
    actions = ActionChains(driver)
    try:
        sku_expend = driver.find_element(By.CLASS_NAME,"sku-wrapper-expend-button")
        
        actions.move_to_element(sku_expend)
        actions.click(sku_expend)
        actions.perform()
    except:
        print('no sku_expend button')

    
    colorList = []
    sku_wrapper = driver.find_element(By.ID,"sku-count-widget-wrapper")
    sku_items = driver.find_elements(By.CLASS_NAME,"sku-item-wrapper")
    # print(sku_items)
    for skus_item in sku_items:
        styleStr = 'no img'
        try:
          styleStr = skus_item.find_element(By.CLASS_NAME,"sku-item-image").get_attribute("style")
        except:
            print("NO image")
            
        url = 'no img url'
        if styleStr != 'no img':
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', styleStr)
            if type(urls) == list:
                url = urls[0]
        title = skus_item.find_element(By.CLASS_NAME,"sku-item-name").text
        # print(title , url)
        colorList.append({"title":title,"url":url})    
    # print(colorList)
    
 
    sizeList = []


    return colorList, sizeList

def login(driver, ele, loginInfo):
    hwnd = win32gui.FindWindow(None, driver.title + " - Google Chrome")
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    if loginInfo is not None:
        if loginInfo['userName']:
            # time.sleep(random.uniform(0.2, 1.2))
            ele.find_element(By.ID, 'fm-login-id').click()
            # time.sleep(random.uniform(0.2, 1.2))
            ele.find_element(By.ID, 'fm-login-id').send_keys(loginInfo['userName'])
        if loginInfo['password']:
            ele.find_element(By.ID, 'fm-login-password').click()
            ele.find_element(By.ID, 'fm-login-password').send_keys(loginInfo['password'])
    else:
        driver.execute_script('alert("未配置登陆账号密码,请扫码登陆");')
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.dismiss()
