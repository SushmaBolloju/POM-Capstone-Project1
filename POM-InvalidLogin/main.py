
from Data import data
from time import sleep

from Locators import locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPage:
   def login(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(3)
        driver.maximize_window()
        sleep(3)
        try:
           input_field = driver.find_element(By.NAME, "username")
           input_field.send_keys("Admin")
           input_field1 = driver.find_element(By.NAME, value="password")
           input_field1.send_keys("edmin123")
           driver.find_element(By.XPATH, value="//button[@type='submit']").click()
           sleep(5)
           print("Entered the invalid login credentials")

        except NoSuchElementException as e:
           print("Error")
        except Exception as e:
           # Handle other exceptions (TimeoutException, WebDriverException, etc.)
           print(f"An error occurred: {e}")

        finally:
           driver.quit()


obj = LoginPage()
obj.login()