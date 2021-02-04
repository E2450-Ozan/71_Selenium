from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/home/Desktop/chromedriver")
base_url = "https://clarusway.com/"
expected_title = "Online Career IT Training School - Clarusway"
actual_title = ""
driver.get(base_url)
actual_title = driver.title
current_url = driver.current_url
print("current url: ", current_url)
# if actual_title == expected_title:
#     print("Test Passed")
# else:
#     print("Test Failed")
#     print(actual_title)