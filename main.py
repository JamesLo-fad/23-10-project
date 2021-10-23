from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

driver = webdriver.Firefox(executable_path=os.getcwd() + "/geckodriver.exe")
driver.get("https://www.bloomberg.com/graphics/global-trade-indicators/")


all_data = []

data_list = driver.find_elements_by_css_selector('.container .indicator.svelte-1kp3mpm')

for data in data_list:
    title = data.find_element_by_css_selector('h5>a').text
    recent_number = data.find_element_by_css_selector('g.bars rect:last-child').get_attribute('data-zscore')
    all_data.append([title, recent_number])
    print(all_data)

driver.close()

print("done")
