from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="/Users/flovearth/Documents/20_Career/19_Workspace/71_Selenium/chromedriver")
base_url = "https://clarusway.com/"
driver.get(base_url)
element = driver.find_element_by_id("EMBED_FORM_EMAIL_LABEL")
element.send_keys("merhaba")
time.sleep(5)
element.clear()
time.sleep(5)
driver.quit()