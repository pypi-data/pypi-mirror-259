from selenium.webdriver.chrome.options import Options
from pathlib import Path
from selenium.webdriver.chrome.service import Service as ChromeDriverService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
import logging
import win32gui, win32com.client


def getDriver():
    print('init driver============')
    # chromedriver_autoinstaller.install()
    # chrome_path = shutil.which("chromedriver")
    # service = Service(executable_path=chrome_path)
    options = Options()
    options.headless = True
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    logger = logging.getLogger(__name__)
    
    if (chromium_driver_path := Path('./chrome_driver_path.txt')).exists():
        with open(chromium_driver_path, 'r') as f:
            chrome_driver_path = f.read()
        chrome_service = ChromeDriverService(str(chrome_driver_path))
    else:
        try:
            chrome_driver = ChromeDriverManager().install()
            with open('./chrome_driver_path.txt', 'w') as f:
                f.write(chrome_driver)
            # print(chrome_driver)
        except AttributeError as e:
            if "'NoneType' object has no attribute 'split'" in str(e):
                # https://github.com/SergeyPirogov/webdriver_manager/issues/649
                logger.critical(
                    "Connecting to browser failed: is Chrome or Chromium installed?"
                )
            raise
        chrome_service = ChromeDriverService(chrome_driver)
    driver = ChromeDriver(service=chrome_service, options=options)
    driver.switch_to.window(driver.current_window_handle)   
    
    return driver

def setToTop(driver):
    hwnd = win32gui.FindWindow(None, driver.title+" - Google Chrome")
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)