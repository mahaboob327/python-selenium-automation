from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the Amazon url
driver.get('https://www.amazon.com/')
sleep(5)

# to Click on Hello, Sign in
driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
sleep(10)

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email
driver.find_element(By.XPATH, "//input[@id='ap_email_login']")
#Continue
driver.find_element(By.XPATH, "//input[@class='a-button-input']")
#Condition of Use
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")
#Privacy Notice
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
# Need Help
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/account-issues/ref=unified_claim_collection?ie=UTF8']")

# Don't see Forgot your password link<<<---
# Don't see Other issues with Sign-In link<<<--

#Create a free business
driver.find_element(By.XPATH, "//a[@id='ab-registration-ingress-link']")
