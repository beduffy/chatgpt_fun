from selenium import webdriver

# Open Chrome and navigate to Google
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find the search input box and enter the search term
search_input = driver.find_element_by_name("q")
search_input.send_keys("rabbits")

# Find the search button and click it
search_button = driver.find_element_by_name("btnK")
search_button.click()