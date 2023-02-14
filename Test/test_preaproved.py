import time
import json
from selenium import webdriver
import unittest
from Actions.preaproveds import *
import unittest, pytest
from ddt import ddt, data, unpack
from Configurations.properties.constans import *
from dotenv import load_dotenv

load_dotenv()

@ddt
class test_preaprovesotherbank(unittest.TestCase):

    def objectSetup(self):
        print('Inicia Test')


    @pytest.mark.run(order=1)
    @data(("5"))
    def test_otherbank(self, idCase):
        with open('Configurations/properties/cases.json') as json_file:
            case = json.load(json_file)[idCase]
        baseUrl = (case[BASEURLPREAPROVADOS])
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        time.sleep(5)
        pre = preaproveds(driver)
        pre.preaprovedsother_banck()
        pre.dates_personal(case[NAME],case[LASTNAME],case[MOBILE],case[EMAIL],case[OTHERPHONE],case[ADRESS],case[AMOUNTSOLI])
        pre.documents()