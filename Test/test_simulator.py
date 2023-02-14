import time
import json
from selenium import webdriver
import unittest
from Actions.Simulator_suite import *
import unittest, pytest
from ddt import ddt, data, unpack
from Configurations.properties.constans import *
from Configurations.drivers.webFactory_logtest import *
from dotenv import load_dotenv

load_dotenv()

@ddt
class test_simula(unittest.TestCase):

    def objectSetup(self):
        print('Inicia Test')

    @pytest.mark.run(order=1)
    @data(("1"),("2"))

    def test_simulator(self,idCase):
        try:
            with open('Configurations/properties/cases.json') as json_file:
                case = json.load(json_file)[idCase]
            baseUrl = (case[BASEURLSIMULADOR])
            webdriver =  Webfactory_lambdaTest(capx,baseUrl)
            driver = webdriver.getWebDriverInstance()
            print(BASEURLSIMULADOR)
            time.sleep(1)
            sim = Simulator(driver)
            sim.select_property(case[NAME_TOWERS])
            sim.enter_personal_data(case[NAME],case[LASTNAME],case[NUMBERDOCUMENT],case[INCOMEUSERFAMILY],case[MOBILE],case[EMAIL])
            if perzonalizeproperty == 'si':
                sim.personalize_property()
            if personalizesubsidy == 'si':
                sim.step_subsidy(case[SIMULACIONWHITSUBSIDY])
            sim.form_payment()
            sim.financial()
            time.sleep(5)
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        except:
            driver.execute_script("lambda-status=failed")
        driver.quit()




















