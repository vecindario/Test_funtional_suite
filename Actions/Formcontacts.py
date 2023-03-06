import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Configurations.properties.constans import *
import Utils.custom_logger as cl
import logging

class Contacts():
    def __init__(self, driver):
        self.driver = driver

    def contacts_trequeri(self,NAME,LASTNAME,MOBILE,EMAIL):
        time.sleep(3)
        self.driver.find_element(By.NAME,"first_name").send_keys(NAME)
        time.sleep(1)
        self.driver.find_element(By.NAME, "last_name").send_keys(LASTNAME)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"form-control").send_keys(MOBILE)
        time.sleep(1)
        self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
        time.sleep(2)

    def other_questions(self,CAPACITY,ADRESS):
        element = self.driver.find_element(By.NAME,"monthly_payment_capacity")
        element.location_once_scrolled_into_view
        self.driver.find_element(By.NAME, "monthly_payment_capacity").send_keys(CAPACITY)
        self.driver.find_element(By.NAME,"city_of_residence").send_keys(ADRESS)
        element1 = self.driver.find_element(By.NAME, "economic_activity")
        element1.location_once_scrolled_into_view
        #self.driver.find_element(By.NAME, "economic_activity").click()
        time.sleep(1)
        #self.driver.find_element(By.XPATH,"//option[@label='Empleado']").click
    def finish(self):
        self.driver.find_element(By.ID,"envio-formulario-cta").click()
        time.sleep(6)