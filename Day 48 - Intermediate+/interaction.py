from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Edge()

# Open a webpage
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

first_name_box = driver.find_element(By.NAME, 'fName')
first_name_box.send_keys("First")
# search_box.send_keys(Keys.ENTER)    # press Enter
last_name_box = driver.find_element(By.NAME, 'lName')
last_name_box.send_keys("Last")

email_box = driver.find_element(By.NAME, 'email')
email_box.send_keys("my_mail@email.com")

sign_up_btn = driver.find_element(By.CSS_SELECTOR, 'body > form > button')
sign_up_btn.click()

# Close the browser
driver.quit()
