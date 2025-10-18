
from selenium import webdriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get('https://www.google.com')
print(driver.title)
driver.quit()