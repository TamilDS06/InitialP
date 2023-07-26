from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time

# Initiate an object.
chrome_driver_path = 'C:\My_Folder\Chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, value='div #articlecount a')
# count = article_count.get_attribute('text')
# print(count)

# Interaction with the webpage (clicking, filling out search bars etc...)
# article_count.click()  # clicking on the ref link
# english_article = driver.find_element(By.LINK_TEXT, value='English')
# english_article.click()
# search = driver.find_element(By.NAME, value='search')
# print(search.get_attribute('name'))
# try:
#     search.send_keys('Python')
#     search.send_keys(Keys.ENTER)
# except StaleElementReferenceException:
#     search.send_keys('Python')
#     search.send_keys(Keys.ENTER)

### Sign_Up challenge ###
# driver.get('https://secure-retreat-92358.herokuapp.com/')
# fName_search = driver.find_element(By.NAME, value='fName')
# lName_search = driver.find_element(By.NAME, value='lName')
# email_search = driver.find_element(By.NAME, value='email')
# # button_sign_up = driver.find_element(By.CLASS_NAME, value='btn-block')
# button_sign_up = driver.find_element(By.CSS_SELECTOR, value='form button')
# try:
#     fName_search.send_keys("Tamilselvan")
#     lName_search.send_keys("Mani")
#     email_search.send_keys('fortest06@gmail.com')
#     button_sign_up.click()
#     time.sleep(5)
# except StaleElementReferenceException:
#     fName_search.send_keys("Tamilselvan")
#     lName_search.send_keys("Mani")
#     email_search.send_keys('fortest06@gmail.com')
#     button_sign_up.click()
#     time.sleep(5)

### Cookie game challenge ###
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(10)
Language_selector_article = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
try:
    Language_selector_article.click()
except StaleElementReferenceException:
    Language_selector_article.click()
cookie = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
time.sleep(10)
# cookies_per_seconds = driver.find_element(By.XPATH, value='//*[@id="cookies"]')
# print(cookies_per_seconds.text.strip())
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
timeout = time.time()
five_min = time.time() + 60*5
while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break