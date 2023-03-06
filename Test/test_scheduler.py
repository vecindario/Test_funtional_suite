import os
import time
import json
from selenium import webdriver
import unittest
from Actions.scheduler import *
import unittest, pytest
from ddt import ddt, data, unpack
from Configurations.properties.constans import *
from Configurations.drivers.webFactory_logtest import *
from dotenv import load_dotenv

if os.environ.get("PYTHON_ENV") != 'production':
    load_dotenv()


@ddt
class tes_scheduler1(unittest.TestCase):

    def objectSetup(self):
        print('Inicia Test')


    @pytest.mark.run(order=1)
    @data(("3"),("4"))
    def test_scheduler(self, idCase):
        try:
            with open('Configurations/properties/cases.json') as json_file:
                case = json.load(json_file)[idCase]
            baseUrl = (case[BASEURLAGENDADOR])
            webdriver = Webfactory_lambdaTest(capx, baseUrl)
            driver = webdriver.getWebDriverInstance()
            time.sleep(5)
            sch = Agendator(driver)
            sch.tipedate(case[TYPE])
            sch.datesuser(case[NAME],case[LASTNAME],case[EMAIL],case[COUNTRY],case[MOBILE])
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")

        except:
            driver.execute_script("lambda-status=failed")
        driver.quit()

