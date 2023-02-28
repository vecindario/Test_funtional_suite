#/usr/bin/python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Configurations.properties.constans import *
import Utils.custom_logger as cl
import logging

class Simulator():



    def __init__(self, driver):
        self.driver = driver

    def select_property(self,NAME_TOWERS):
        #self.driver.find_element(By.XPATH,"(//select[@id='select-floor-1'])[1]").click()
        #select = Select(self.driver.find_element(By.ID,"select-floor-1"))
        #select.select_by_value("2")
        #time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[text()='"+NAME_TOWERS+"']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//input[@id='simula-cta'])[1]").click()
        time.sleep(5)
    def enter_personal_data(self,NAME,LASTNAME,NUMBERDOCUMENT,INCOMEUSERFAMILY,MOBILE,EMAIL):
        self.driver.find_element(By.NAME,"name").send_keys(NAME)
        self.driver.find_element(By.NAME,"lastname").send_keys(LASTNAME)
        time.sleep(1)
        select_document = Select(self.driver.find_element(By.NAME, "documentType"))
        select_document.select_by_value("CE")
        self.driver.find_element(By.NAME,"documentNumber").send_keys(NUMBERDOCUMENT)
        select_income = Select(self.driver.find_element(By.NAME, "economicActivity"))
        select_income.select_by_value("other_activity")
        self.driver.find_element(By.NAME,"userFamilyIncome").send_keys(INCOMEUSERFAMILY)
        self.driver.find_element(By.ID, "mobile").send_keys(MOBILE)
        self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
        time.sleep(1)
        element = self.driver.find_element(By.ID, "contacto-cta")
        element.location_once_scrolled_into_view
        self.driver.find_element(By.ID,"contacto-cta").click()
        time.sleep(1)
    def personalize_property(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//p[text()='¿Quieres agregar un parqueadero?']").click()
        select_parking = Select(self.driver.find_element(By.NAME, "parking"))
        select_parking.select_by_value("50c01d0d-a6de-46fa-a87d-136797688362")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//p[text()='¿Quieres agregar un cuarto útil?']").click()
        select_useful = Select(self.driver.find_element(By.NAME, "useful_room"))
        select_useful.select_by_value("1a5d1f82-c25d-42b2-b8eb-20b5890a673f")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//p[text()='¿Quieres agregar acabados?']").click()
        select_fishish = Select(self.driver.find_element(By.NAME, "finish"))
        select_fishish.select_by_value("548a3664-4b40-4a00-a1bc-2b695eb8b5d8")
        time.sleep(1)
        self.driver.find_element(By.ID,"personaliza-tu-inmueble-cta").click()

    def step_subsidy(self,SIMULACIONWHITSUBSIDY):
        subsidy = SIMULACIONWHITSUBSIDY
        if subsidy == 'si':
            select_subsidy = Select(self.driver.find_element(By.ID, "apply_subsidy"))
            select_subsidy.select_by_value("si")
            time.sleep(1)
            select_home = Select(self.driver.find_element(By.ID, "already_has_home"))
            select_home.select_by_value("no")
            time.sleep(1)
            select_subsidy = Select(self.driver.find_element(By.ID, "already_has_subsidy"))
            select_subsidy.select_by_value("no")
            time.sleep(1)
            select_box = Select(self.driver.find_element(By.ID, "compensation_fund"))
            select_box.select_by_value("si")
            time.sleep(1)
            self.driver.find_element(By.ID,"compensation_fund_name").send_keys(CAJACOMPENSACION)
            time.sleep(1)
        else:
            select_subsidy = Select(self.driver.find_element(By.ID, "apply_subsidy"))
            select_subsidy.select_by_value("si")
            time.sleep(1)
            select_home = Select(self.driver.find_element(By.ID, "already_has_home"))
            select_home.select_by_value("si")
            time.sleep(1)
            select_subsidy = Select(self.driver.find_element(By.ID, "already_has_subsidy"))
            select_subsidy.select_by_value("si")
            time.sleep(1)
            select_box = Select(self.driver.find_element(By.ID, "compensation_fund"))
            select_box.select_by_value("si")
        element4 = self.driver.find_element(By.ID, "subsidio-de-vivienda-cta")
        element4.location_once_scrolled_into_view
        self.driver.find_element(By.ID, "subsidio-de-vivienda-cta").click()
        time.sleep(3)
    def form_payment(self):
        self.driver.find_element(By.XPATH,"(//input[@type='tel'])[1]").send_keys("0")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//label[@name='yes-savings'])[2]").click()
        time.sleep(1)
        element1 = self.driver.find_element(By.XPATH, "(//div[@class='toggle__container '])[1]")
        element1.location_once_scrolled_into_view
        self.driver.find_element(By.XPATH,"(//div[@class='toggle__container '])[1]").click()
        element2 = self.driver.find_element(By.NAME, "currency")
        element2.location_once_scrolled_into_view
        self.driver.find_element(By.NAME,"currency").send_keys(PRIMAS)
        element3 = self.driver.find_element(By.XPATH, "(//div[@class='toggle__container '])[2]")
        element3.location_once_scrolled_into_view
        time.sleep(6)
        self.driver.find_element(By.XPATH,"(//div[@class='toggle__container '])[2]").click()
        self.driver.find_element(By.XPATH,"(//input[@name='currency'])[2]").send_keys(CESANTIAS)
        element4 = self.driver.find_element(By.XPATH, "(//div[@class='toggle__container '])[3]")
        element4.location_once_scrolled_into_view
        self.driver.find_element(By.XPATH, "(//div[@class='toggle__container '])[3]").click()
        self.driver.find_element(By.XPATH, "(//input[@name='currency'])[3]").send_keys(CUOTASPERZONA)
        element5 = self.driver.find_element(By.ID, "forma-de-pago-cta")
        element5.location_once_scrolled_into_view
        self.driver.find_element(By.ID,"forma-de-pago-cta").click()

    def financial(self):
        self.driver.find_element(By.ID,"generar-simulación-financiación-cta").click()
        time.sleep(2)






