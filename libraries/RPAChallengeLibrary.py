from robot.api.deco import keyword
from robot.api import logger


from resources.locators import Locators
from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    run_kw,
    get_variable,
)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class RPAChallengeLibrary(LibraryBase):
    """
    Template for implementing a robot library.
    """

    def __init__(self):
        super().__init__()
      
        # muuttujat resources/settings
        self.env = get_variable("${ENV}")

  #     OPEN WEB PAGE
        #
        self.options = webdriver.ChromeOptions()
        #self.driver = webdriver.ChromeOptions()
        #self.driver.get_variable("${rpa_challenge_url}")
        self.rpa_challenge_url = get_variable("${rpa_challenge_url}")
        self.downloads_path = get_variable("${download_path}")
        self.download_url = get_variable("${download_url}")

    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()

    ## tähän driver -komento downloadamiseen

    @keyword
    def download_rpa_excel(self):
        self.browser.download(self.download_url)

    # OPEN BROWSER
    @keyword
    def go_to_rpa_challenge(self):
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
        options=self.options, executable_path=r'C:\Users\Omistaja\Documents\webdrivers\chromedriver.exe')
        self.driver.get(self.rpa_challenge_url)

    @keyword
    def start_challenge(self):
        self.driver.find_element(By.XPATH,Locators.start_button ).click()
    
    # muuttujat resources/locators
    @keyword  
    def insert_first_name(self, first_name):
        first_name_element = self.driver.find_element(
            By.XPATH, Locators.first_name)
        # kutsun stagesta insert_name - annetaan task objectin avain-arvoparin
        first_name_element.send_keys(first_name)

    @keyword
    def insert_last_name(self, last_name):
        last_name_element = self.driver.find_element(By.XPATH, Locators.last_name)
        last_name_element.send_keys(last_name)

    @keyword
    def insert_company_name(self, company_name):
        company_name_element = self.driver.find_element(By.XPATH, Locators.company_name)
        company_name_element.send_keys(company_name)

    @keyword
    def insert_role_in_company(self, role_in_company):
        role_in_company_element = self.driver.find_element(
            By.XPATH, Locators.role_in_company)
        role_in_company_element.send_keys(role_in_company)

    @keyword
    def insert_address(self, address):
        address_element = self.driver.find_element(By.XPATH, Locators.address)
        address_element.send_keys(address)

    @keyword
    def insert_email(self, email):
        email_element = self.driver.find_element(By.XPATH, Locators.email)
        email_element.send_keys(email)

    @keyword
    def insert_phone_number(self, phone_number):
        phone_number_element = self.driver.find_element(By.XPATH, Locators.phone_number)
        phone_number_element.send_keys(str(phone_number))

    @keyword
    def click_submit(self):
        self.driver.find_element(By.XPATH, Locators.submit_button).click()

    @keyword
    def close_rpa_challenge(self):
        self.driver.quit()

    @keyword
    def do_something(self):
        run_kw("Log", f"Doing something in {self.env}")
