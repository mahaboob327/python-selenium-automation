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

# open the Target url
driver.get('https://www.target.com/')
sleep(5)
#need to click Health Data Consent Click Continue shopping
driver.find_element(By.XPATH, "//button[@id='VA_HEALTH_CONSENT_BUTTON']").click()
sleep(5)

# to Click on Account, Sign in
driver.find_element(By.XPATH, "//span[@class='sc-1a162949-3 iuQwR display-name h-margin-r-x3']").click()
sleep(7)
#Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# Check for "Sign in or create account" text
driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in or create account')]")

sleep(5)
driver.quit()

