
from Data import data
from Locators import locator
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
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
           input_field = self.driver.find_element(By.NAME, "username")
           input_field.send_keys("Admin")
           input_field1 = self.driver.find_element(By.NAME, value="password")
           input_field1.send_keys("admin123")

           self.driver.find_element(By.XPATH, value="//button[@type='submit']").click()
           print("Entered the valid login credentials")


       except NoSuchElementException as e:
       # Handle the case where the element is not found
            print(f"Element not found: {e}")

       except Exception as e:
    # Handle other exceptions (TimeoutException, WebDriverException, etc.)
            print(f"An error occurred: {e}")

       finally:
    # Optional: Perform cleanup or close the WebDriver instance
             self.driver.quit()

obj = LoginPage()
obj.login()
