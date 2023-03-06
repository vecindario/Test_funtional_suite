#/usr/bin/python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Configurations.properties.constans import *
import Utils.custom_logger as cl
import logging

class landingbuilder():



    def __init__(self, driver):
        self.driver = driver

    def info_landing_simulator(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='navbar-item'])[1]").click()
        time.sleep(2)

    def info_landing_shelude(self):
        element1 = self.driver.find_element(By.XPATH, "(//h1[@class='poppins title '])[2]")
        element1.location_once_scrolled_into_view
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Agenda tu cita aquí']").click()
        time.sleep(9)
        thakyou = self.driver.find_element(By.XPATH,"//h1[text()='Solicita una cita con un asesor']").text
        print(thakyou)
        assert "Solicita una cita con un asesor" == thakyou
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"ri-close-line").click()
        time.sleep(3)
    def info_landing_contacts(self):
        element2 = self.driver.find_element(By.XPATH, "//h4[contains(@class,'container-text color-secondary-900t')]")
        element2.location_once_scrolled_into_view
        time.sleep(2)
        thakyou1 = self.driver.find_element(By.XPATH,"//h4[contains(@class,'container-text color-secondary-900t')]").text
        print(thakyou1)
        time.sleep(1)
        assert "Déjanos tus datos para compartirte más información del proyecto" in thakyou1.encode("utf-8")
        time.sleep(1)
    def info_landing_galery(self):
        self.driver.find_element(By.XPATH,"(//div[@class='navbar-item'])[2]").click()
        time.sleep(1)
        galery = self.driver.find_element(By.XPATH,"(//a[@data-lightbox='roadtrip']//img)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"lb-close").click()
        time.sleep(2)

    def info_landing_maps(self):
        self.driver.find_element(By.XPATH,"(//div[@class='navbar-item'])[3]").click()
        time.sleep(1)
        thakyou3 = self.driver.find_element(By.XPATH,"(//h2[@class='poppins title'])[2]").text
        print(thakyou3)
        time.sleep(2)
        assert "Ubicación real del proyecto" == thakyou3.encode("utf-8")
        time.sleep(1)