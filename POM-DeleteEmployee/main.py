from Data import data
from Locators import locator
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPage:
    def del_emp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
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
            driver.find_element(By.XPATH, value="(//i[@class='oxd-icon bi-trash'])[1]").click()
            sleep(5)
            driver.find_element(By.XPATH,value="//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
            sleep(5)


        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            raise  # Re-raise the exception

        except Exception as e:
            print(f"An error occurred during login: {e}")
            raise  # Re-raise the exception
        finally:
            # Optional: Perform cleanup or close the WebDriver instance
            driver.quit()

obj = LoginPage()
obj.del_emp()