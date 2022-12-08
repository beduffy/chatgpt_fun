# Prompt: Selenium code for going to ryanair and searching for a flight to Madagascar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start a new Chrome web driver
driver = webdriver.Chrome()

# Go to the Ryanair website
driver.get('https://www.ryanair.com/')

# Click the "Flights" tab
flights_tab = driver.find_element_by_id('tab-flights')
flights_tab.click()

# Enter "Madagascar" as the destination
destination_field = driver.find_element_by_id('destination')
destination_field.send_keys('Madagascar')

# Click the "Search" button
search_button = driver.find_element_by_id('search-button')
search_button.click()