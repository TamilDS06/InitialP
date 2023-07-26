from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


# Initiate an object.
chrome_driver_path = 'C:\My_Folder\Chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit")
time.sleep(3)

# Login
def log_in():
    main_sign_in_link = driver.find_element(By.CLASS_NAME, value='main__sign-in-link')
    main_sign_in_link.click()
    time.sleep(3)
    enter_email_or_phone = driver.find_element(By.NAME, value='session_key')
    enter_email_or_phone.send_keys("mtsmech04@gmail.com")
    enter_password = driver.find_element(By.NAME, value='session_password')
    enter_password.send_keys("Linkedtamilin")
    sign_in_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
    sign_in_button.click()

# Search for our requirement job and Apply for the job with "Easy apply functionality".
def search_apply_for_job():
    try:
        search_global = driver.find_element(By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
        search_global.send_keys("Python developer")
        search_global.send_keys(Keys.ENTER)
        time.sleep(10)
        eassy_apply = driver.find_element(By.CLASS_NAME, value='app-aware-link')
        eassy_apply.click()
        first_search_result = driver.find_element(By.XPATH, value='//*[@id="YJNN7I+xQUm3gg0HciXo9A=="]/div/ul[2]/li[1]/div/div/div[2]/div[1]/div[1]/div/span/span/a')
        first_search_result.click()
        time.sleep(15)
    except NoSuchElementException:
        log_out()

# Logout
def log_out():
    profile_button = driver.find_element(By.XPATH, value='//*[@id="ember15"]')
    profile_button.click()
    logout_button = driver.find_element(By.XPATH, value='//*[@id="ember16"]')
    logout_button.click()

if __name__ == "__main__":
    log_in()
    search_apply_for_job()
    log_out()