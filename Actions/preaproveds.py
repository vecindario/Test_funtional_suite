import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Configurations.properties.constans import *
import Utils.custom_logger as cl
import logging

class preaproveds():
    def __init__(self, driver):
        self.driver = driver

    def preaprovedsother_banck(self):
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        notnows =  self.driver.find_elements(By.CSS_SELECTOR,"div#root>section>div>div:nth-of-type(2)>div>section>a")
        for notnow in notnows:
            notnow.click()
        time.sleep(1)
        notnows1 = self.driver.find_elements(By.CSS_SELECTOR,"div#root>section>div>div:nth-of-type(2)>div>div:nth-of-type(2)>section")
        for notnow1 in notnows1:
            notnow1.click()
        time.sleep(1)

    def dates_personal(self,NAME,LASTNAME,MOBILE,EMAIL,OTHERPHONE,ADRESS,AMOUNTSOLI):
        self.driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys(NAME)
        self.driver.find_element(By.NAME,"last_name").send_keys(LASTNAME)
        self.driver.find_element(By.NAME,"mobile").send_keys(MOBILE)
        self.driver.execute_script("window.scrollBy(0,100)")
        time.sleep(2)
        self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.NAME, "phone").send_keys(OTHERPHONE)
        self.driver.find_element(By.NAME,"address").send_keys(ADRESS)
        self.driver.find_element(By.NAME,"amountCredit").send_keys(AMOUNTSOLI)
        time.sleep(3)
    def documents(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        filepath= "C:\\Users\\34643\\Pictures\\Screenshots\\Atitlan-Menu-Banner.jpg"
        file_tag_list = self.driver.find_element(By.XPATH,"//input[@name ='front_document_identification' and @type='file']")
        file_tag_list.send_keys(filepath)
        time.sleep(2)
        filepathtwo = "C:\\Users\\34643\\Pictures\\Screenshots\\Atitlan-Menu-Banner.jpg"
        file_tag_listtwo = self.driver.find_element(By.XPATH,"//input[@name ='back_document_identification' and @type='file']")
        file_tag_listtwo.send_keys(filepathtwo)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//input[@class='suite-checkbox check-box-form'])[1]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='suite-checkbox check-box-form'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
