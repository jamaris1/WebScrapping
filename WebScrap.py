from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time
import random



WAIT_TIME = 100

BestBuyURL = 'https://listado.mercadolibre.com.co/tarjeta-de-video#D[A:tarjeta%20de%20video]'

class Bote:



    def __init__(self):
        self.driver = webdriver.Edge(executable_path='C:\\Program Files (x86)\\edgedriver_win32\\msedgedriver.exe')
        #self.driver = webdriver.Chrome(executable_path='C:\\Users\\jamar\\Downloads\\chromedriver_win32\\chromedriver.exe')


    def signIn(self):
        driver = self.driver
        driver.get(BestBuyURL)
        print(driver.current_url)
        username_elem = driver.find_element_by_class_name("addToCartContainer_20u-G")
        time.sleep(int(WAIT_TIME/2))
        username_elem
        username_elem.click()
        time.sleep(int(WAIT_TIME))

