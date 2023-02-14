from selenium import webdriver
from Configurations.properties.constans import *
import logging



class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        self.log.info(self.browser)
        print(self.browser)
        if self.browser == "iexplorer":
            self.log.warning("### Navegador no soportado")
            # cap = DesiredCapabilities().INTERNETEXPLORER
            # cap['ignoreZoomSetting'] = True
            # driver = webdriver.Ie(capabilities=cap, executable_path=r'd:\\IEDriver\\IEDriverServer.exe')
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
            #driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(BASEURL)
        return driver

