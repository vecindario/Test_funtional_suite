import os
from selenium import webdriver
from Configurations.properties.constans import *
from Configurations.properties.properties_users import *
from dotenv import load_dotenv

if os.environ.get("PYTHON_ENV") != 'production':
    load_dotenv()

class Webfactory_lambdaTest():

    def __init__(self, cap,baseurl):
        self.cap = cap
        self.baseurl = baseurl

    def getWebDriverInstance(self):
        try:
            print("start webdriver")
            username = os.environ.get("USERNAME")  # Replace the username
            access_key = os.environ.get("ACCES_KEY")  # Replace the access key
            desired_caps = {
                'LT:Options': {
                    "build": "Python Demo",  # Change your build name here
                    "name": "Python Demo Test",  # Change your test name here
                    "platformName": "Windows 11",
                    "selenium_version": "4.0.0",
                    "console": 'true',  # Enable or disable console logs
                    "network": 'true',  # Enable or disable network logs
                    # Enable Smart UI Project
                    # "smartUI.project": "<Project Name>"
                },
                "browserName": "chrome",
                "browserVersion": "latest",
            }

            print(self.cap)
            url = "https://" + username_lbtest + ":" + accessToken_lbtest + "@" + gridUrl_lbtest
            driver = webdriver.Remote(
                command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                    username, access_key),
                desired_capabilities=desired_caps)


            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(self.baseurl)
            return driver
        except Exception:
            raise Exception("Unable to load google page!")


