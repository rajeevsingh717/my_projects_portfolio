import pandas as pd
import selenium as sl
import time


from selenium import webdriver
username = '****ji@gmail.com'
password = '****'

driver = webdriver.Chrome(executable_path="/Users/rajeevsingh/Documents/PythonProjects/chromedriver")
time.sleep(2)
driver.maximize_window()

driver.get("https://www.linkedin.com/")

### Signing in 
time.sleep(2)
driver.find_element_by_link_text("Sign in").click()
time.sleep(2)
userinput = driver.find_element_by_id("username")
userinput.send_keys(username)
passwordinput = driver.find_element_by_id("password")
passwordinput.send_keys(password)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()


time.sleep(2)
## Click on the job Icon
driver.find_element_by_link_text("Jobs").click()

time.sleep(2)
##Minimize the chat window
driver.find_element_by_css_selector('[class="msg-overlay-bubble-header"]').click()


## Click on Data Engineer
time.sleep(2)
driver.find_element_by_xpath('//*[@title="data engineering"]').click()
#driver.find_element_by_xpath('//*[@title="data analyst"]').click() #Seaach for data analyst job



## Retrieving the data
html_list = driver.find_element_by_css_selector('[class="jobs-search-results__list list-style-none"]')
items = html_list.find_elements_by_tag_name("li")

text_x = ''
for item in items:
    print(item.get_attribute("innerHTML"))
    text_x += '<------------------------------------------------->'
    text_x +=  item.get_attribute("innerHTML")


## Writing the xml into local file

file = open("//Users//rajeevsingh//Documents//PythonProjects//file1.txt", "w")
file.write(text_x)
file.close()



#driver.refresh()
#driver.close()
