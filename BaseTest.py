import unittest
from selenium import webdriver
import os
from appium import webdriver

class BaseTest(unittest.TestCase):

    __BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    __APP_PATH = os.path.join(__BASE_DIR, '.app/app-qa-debug.apk')

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Galaxy A3'
        desired_caps['app'] = 'C:/Users/Vadim/Desktop/ap_qa_debug/app-qa-debug.apk'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):

        print(self.__APP_PATH)
        pass