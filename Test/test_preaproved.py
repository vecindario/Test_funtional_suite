import os
import time
import json
from selenium import webdriver
import unittest
from Actions.preaproveds import *
import unittest, pytest
from ddt import ddt, data, unpack
from Configurations.properties.constans import *
from dotenv import load_dotenv
from Configurations.drivers.webFactory_logtest import *

if os.environ.get("PYTHON_ENV") != 'production':
    load_dotenv()

@ddt
class test_preaprovesotherbank(unittest.TestCase):

    def objectSetup(self):
        print('Inicia Test')


    @pytest.mark.run(order=1)
    @data(("5"))
    def test_otherbank(self, idCase):
        try:
            with open('Configurations/properties/cases.json') as json_file:
                case = json.load(json_file)[idCase]
            baseUrl = (case[BASEURLPREAPROVADOS])
            webdriver = Webfactory_lambdaTest(capx, baseUrl)
            driver = webdriver.getWebDriverInstance()
            time.sleep(5)
            pre = preaproveds(driver)
            pre.preaprovedsother_banck()
            pre.dates_personal(case[NAME],case[LASTNAME],case[MOBILE],case[EMAIL],case[OTHERPHONE],case[ADRESS],case[AMOUNTSOLI])
            pre.documents()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        except:
            driver.execute_script("lambda-status=failed")

        driver.quit()