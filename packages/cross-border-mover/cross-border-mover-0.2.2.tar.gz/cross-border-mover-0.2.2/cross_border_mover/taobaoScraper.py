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
def getSKUInfo(url, loginInfo):

    driver = driver1.getDriver()

    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver1.setToTop(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(random.uniform(0.2, 1.2))
    
    try:
        loginBtn = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME,"SecurityContent--loginBtn--28e5PZf"))) 
        loginBtn.click() 
    except:
        print("loginBtn===========no")



    if driver.title == '淘宝网 - 淘！我喜欢':
        # print(driver.title)
        login(driver, loginInfo)


    
    skuWrapper = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"skuWrapper")))
    colorList = []
    skuItemWrappers = skuWrapper.find_elements(By.CLASS_NAME,"skuItemWrapper")
    sku_items = skuItemWrappers[0].find_elements(By.CLASS_NAME,"skuItem")
    # print(sku_items)
    for skus_item in sku_items:
        styleStr = 'no img'
        try:
            styleStr = skus_item.find_element(By.CLASS_NAME,"skuIcon").get_attribute("src")
        except:
            print("NO image")
            
        url = 'no img url'
        if styleStr != 'no img':
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', styleStr)
            if type(urls) == list:
                url = urls[0]
                url = url.replace('60x60q50', '1200x1200q90')
        title = skus_item.find_element(By.CLASS_NAME,"skuValueName").text
        # print(title , url)
        colorList.append({"title":title,"url":url})    
    # print(colorList)


    sizeList = []
    if len(skuItemWrappers) > 1: 
        sku_sizes = skuItemWrappers[1].find_elements(By.CLASS_NAME,"skuItem")
        for sku_size in sku_sizes:
            size_text = sku_size.find_element(By.CLASS_NAME,"skuValueName").text
            sizeList.append(size_text)
        
    # print(sizeList)
    # driver.quit()

    return colorList,sizeList
    
def login(driver, loginInfo):
    print('login=========')
    try:
        hwnd = win32gui.FindWindow(None, "淘宝网 - 淘！我喜欢 - Google Chrome")
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)
    except:
        print("hwnd===========no")
    # loginBtn = driver.find_element(By.CLASS_NAME,"SecurityContent--loginBtn--28e5PZf")
    # print(loginBtn)
    # loginBtn.click()
    if loginInfo is not None:
        if loginInfo['userName']:
            # time.sleep(random.uniform(0.2, 1.2))
            driver.find_element(By.ID, 'fm-login-id').click()
            # time.sleep(random.uniform(0.2, 1.2))
            driver.find_element(By.ID, 'fm-login-id').send_keys(loginInfo['userName'])
        if loginInfo['password']:
            # time.sleep(random.uniform(0.2, 1.2))
            driver.find_element(By.ID, 'fm-login-password').click()
            # time.sleep(random.uniform(0.2, 1.2))
            driver.find_element(By.ID, 'fm-login-password').send_keys(loginInfo['password'])
    else:
        driver.execute_script('alert("未配置登陆账号密码,请扫码登陆");')
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.dismiss()
    print('login=========end')
    