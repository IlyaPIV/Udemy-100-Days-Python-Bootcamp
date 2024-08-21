from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Edge()

# Open a webpage
driver.get("https://www.python.org")

# elem = driver.find_element(By.NAME, "q")
# print(elem.tag_name)
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)
#
# status_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
# print(status_link.text)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery ul li")

events_list = {}

for n in range(len(events)):
    event = events[n]
    event_data = event.text.split("\n")
    events_list[n] = {
        "time": event_data[0],
        "name": event_data[1],
    }

print(events_list)

# Close the browser
driver.quit()
