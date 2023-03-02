import time
import json
from selenium import webdriver
import unittest
from Actions.Formcontacts import *
import unittest, pytest
from ddt import ddt, data, unpack
from Configurations.properties.constans import *
from Configurations.drivers.webFactory_logtest import *
from selenium.webdriver.chrome.service import Service
from Actions.Landingpage import landingbuilder
from Configurations.drivers.webFactory_logtest import *
@ddt
class test_contact(unittest.TestCase):

    def objectSetup(self):
        print('Inicia Test')


    @pytest.mark.run(order=1)
    @data(("14"))
    def test_contac(self, idCase):
        try:
            with open('Configurations/properties/cases.json') as json_file:
                case = json.load(json_file)[idCase]
                baseUrl = (case[BASEURLCONTACT])
                webdriver = Webfactory_lambdaTest(capx, baseUrl)
                driver = webdriver.getWebDriverInstance()
                time.sleep(4)
                driver.maximize_window()
                lan = landingbuilder(driver)
                lan.info_landing_simulator()
                lan.info_landing_shelude()
                lan.info_landing_contacts()
                lan.info_landing_galery()
                lan.info_landing_maps()
                driver.execute_script("lambda-status=passed")
                print("Tests are run successfully!")
        except:
            driver.execute_script("lambda-status=failed")

        driver.quit()
