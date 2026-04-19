from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup')
sleep(2)

# CSS selector, class
driver.find_element(By.CSS_SELECTOR, "h1.fs-headline1")

# CSS selector, class Terms of service
driver.find_element(By.CSS_SELECTOR, '.js-terms')

# CSS selector, using id for Email
driver.find_element(By.CSS_SELECTOR, '#email')

# CSS selector, using id for Password
driver.find_element(By.CSS_SELECTOR, '#password')

#icon
driver.find_element(By.CSS_SELECTOR, 'svg.js-show-password')

#Sign up
driver.find_element(By.CSS_SELECTOR, '#submit-button')

# Sign up with Google, class Terms of service
driver.find_element(By.CSS_SELECTOR, "button.s-btn__google")


# Sign up with GitHub, class Terms of service
driver.find_element(By.CSS_SELECTOR, "button.s-btn__github")

# Get Stack OverFlow free link
driver.find_element(By.CSS_SELECTOR, "a[href*='stackoverflow.com/teams']")
