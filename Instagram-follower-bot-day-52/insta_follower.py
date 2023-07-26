from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from constant import Constant
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=Constant.CHROME_DRIVER_PATH))
    

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(Constant.USER_NAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(Constant.PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        time.sleep(5)


    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{Constant.ACCOUNT_TO_FOLLOW}/')
        time.sleep(5)
        total_followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_PZ"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span')
        total_followers.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
        

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


    # def logout(self):
    #     log_out = self.driver.find_elements(By.XPATH, value='//*[@id="mount_0_0_TN"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div/div/div/svg')
    #     log_out.click()

        