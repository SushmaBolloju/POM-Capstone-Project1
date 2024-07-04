from Data import data
from time import sleep
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

   def quit(self):
       self.driver.quit()

   def login(self):
       try:
           self.boot()
           # Wait for the username field to be visible
           username_field =self.driver.find_element(By.NAME, "username")
           username_field.send_keys("Admin")

           # Locate and enter password
           password_field = self.driver.find_element(By.NAME, value="password")
           password_field.send_keys("admin123")

           # Click on the login button
           login_button = self.driver.find_element(By.XPATH, value="//button[@type='submit']")
           login_button.click()

           # Wait for the PIM module link to be clickable and click it
           pim_module_link = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
           pim_module_link.click()

           # Click on the Add button to add a new employee
           add_employee_btn = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
           add_employee_btn.click()
           sleep(3)

           # Fill in employee details
           fname = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
           fname.send_keys("lilly")
           Lname = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
           Lname.send_keys("Rosy")
           empid = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
           empid.send_keys("3456")

           # Save the employee details
           save = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
           save.click()
           sleep(5)
           personal_detail = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
           personal_detail.click()
           sleep(2)
           nationality = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
           nationality.click()
           sleep(2)
           n1 = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
           n1.send_keys("Namibian")
           sleep(2)
           n2 = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
           n2.click()
           sleep(2)

           marital_status = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')
           marital_status.click()
           sleep(2)
           m1 = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
           m1.send_keys("married")
           sleep(2)

           otherid = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]")
           otherid.send_keys("7864")
           sleep(2)
           licence = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")
           licence.send_keys("7941")
           sleep(3)
           expiry_date = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
           expiry_date.send_keys("2024-04-05")
           sleep(5)
           birth_date = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
           birth_date.send_keys("1992-10-12")
           sleep(2)
           gender = self.driver.find_element(By.XPATH, "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']")
           gender.click()

           sleep(2)
           # saving the details
           self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
           sleep(3)

       except NoSuchElementException as e:
           print("Error!")
       finally:
           self.quit()


obj = LoginPage()
obj.login()