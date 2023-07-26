from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Documentation # https://selenium-python.readthedocs.io/
from selenium.webdriver.common.by import By

# Initiate an object.
chrome_driver_path = 'C:\My_Folder\Chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
# driver.get("https://www.amazon.com")
# driver.get('https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6')
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# print(price)
# driver.get('https://www.python.org/')
# print(driver.find_element(by='name', value='q').get_attribute('class'))  # Find element using name
# print(driver.find_element(By.CSS_SELECTOR, value='div .slide-copy p a').get_attribute('href'))  # Find element using CSS selector
#
# print(driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a').get_attribute('href'))  # Find
# element using xpath # https://www.w3schools.com/xml/xpath_intro.asp


### Challenge ###

driver.get('https://www.python.org/')
date = [element.text for element in driver.find_elements(By.CSS_SELECTOR, value='div .event-widget div ul li time')]
events = [element.text for element in driver.find_elements(By.CSS_SELECTOR, value='div .event-widget div ul li a')]
event_time_dict = {}
event_count = 0
for date, event in zip(date, events):
    event_time = {'time': date, 'name': event}
    event_time_dict[event_count] = event_time
    event_count += 1
print(event_time_dict)

