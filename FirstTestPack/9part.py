from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="/Users/flovearth/Documents/20_Career/19_Workspace/71_Selenium/chromedriver")
base_url = "https://clarusway.com/"
driver.get(base_url)

time.sleep(3)

element = driver.find_element_by_id("menu-item-2808")
print("aws-devops butonu gösteriliyor mu? ---> ", element.is_displayed())
time.sleep(5)
driver.quit()