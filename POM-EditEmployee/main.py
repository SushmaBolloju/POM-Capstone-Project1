from Data import data
from Locators import locator
from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPage:

    def login(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        sleep(3)
        driver.maximize_window()
        sleep(3)
        try:
            driver.find_element(By.NAME, value="username").send_keys("Admin")
            sleep(2)
            driver.find_element(By.NAME, value="password").send_keys("admin123")
            sleep(2)
            driver.find_element(By.XPATH, value="//button[@type='submit']").click()
            sleep(4)
            driver.find_element(By.LINK_TEXT, value="PIM").click()
            sleep(5)
            driver.find_element(By.LINK_TEXT, value="Employee List").click()
            sleep(5)
            driver.find_element(By.XPATH, value="(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
            sleep(5)
            driver.find_element(By.NAME, value="firstName").clear()
            sleep(5)
            driver.find_element(By.NAME, value="firstName").send_keys("Priyanka")
            sleep(5)
            driver.find_element(By.NAME, value="middleName").clear()
            sleep(3)
            driver.find_element(By.NAME, value="middleName").send_keys("Magesh")
            sleep(3)
            driver.find_element(By.NAME, value="lastName").clear()
            sleep(2)
            driver.find_element(By.NAME, value="lastName").send_keys("K")
            sleep(2)
            driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
            sleep(2)
            driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()


        # def __init__(self):
   #     self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   #
   # def boot(self):
   #     self.driver.get(data.WebData().url)
   #     self.driver.maximize_window()
   #     self.driver.implicitly_wait(10)
   #
   # def quit(self):
   #     self.driver.quit()
   #
   # def login(self):
   #     try:
   #         self.boot()
   #         locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
   #         locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
   #         locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().clickButton(self.driver,locator.WebLocators().buttonLocator1)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().enterText(self.driver,locator.WebLocators().empnameLocator,data.WebData().empname)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().clickButton(self.driver,locator.WebLocators().searchbuttonLocator)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().clickButton(self.driver,locator.WebLocators().editbuttonLocator)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().enterText(self.driver,locator.WebLocators().middlenameLocator,data.WebData().middlename)
   #         self.driver.implicitly_wait(10)
   #         locator.WebLocators().clickButton(self.driver,locator.WebLocators().savebutton2Locator)
   #         self.driver.implicitly_wait(10)
   #         print("Success !!")


        except NoSuchElementException as e:
            print("Error!")
        finally:
            driver.quit()


obj = LoginPage()
obj.login()