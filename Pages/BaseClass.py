from selenium import webdriver


class BaseClass(object):


    def __init__(self, driver):
        self.driver = driver