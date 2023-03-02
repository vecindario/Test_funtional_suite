import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Configurations.properties.constans import *
import Utils.custom_logger as cl
import logging

class Agendator():
    def __init__(self, driver):
        self.driver = driver

    def tipedate(self,TYPE):
        typedate = TYPE
        if typedate == "fisica":
            self.driver.find_element(By.XPATH,"(//div[@class='SelectCard_select-card__3rpiq '])[1]").click()
        if typedate == "digital":
            self.driver.find_element(By.XPATH,"(//div[@class='SelectCard_select-card__3rpiq '])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//p[@class='DateCard_monthday__3o2Jp'])[3]").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//div[@class='HourSelect_hour__1HVfQ'])[1]").click()
        #self.driver.find_element(By.ID,"seleccion-horario-cta").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)

    def datesuser(self,NAME,LASTNAME,EMAIL,COUNTRY,MOBILE):
        time.sleep(2)
        self.driver.find_element(By.NAME,"name").send_keys(NAME)
        self.driver.find_element(By.NAME, "lastname").send_keys(LASTNAME)
        self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
        self.driver.find_element(By.XPATH,"(//div[@role='button']//div)[1]").click()
        self.driver.find_element(By.CLASS_NAME,"search-box").send_keys(COUNTRY)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//li[@data-country-code='es']").click()
        self.driver.find_element(By.CLASS_NAME,"form-control").send_keys(MOBILE)
        self.driver.find_element(By.ID,"agendar-cta").click()
        time.sleep(10)
        thankyou = self.driver.find_element(By.XPATH, "//h2[@class='Header_day__X2wUu font-text']").text
        print(thankyou)
        assert "Te esperamos" in thankyou
        time.sleep(2)