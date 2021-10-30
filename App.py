from flask import Flask, make_response, send_file, send_from_directory, safe_join, abort
import os
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)


@app.route("/information/")
def information():

    from selenium.webdriver.firefox.options import Options
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.service import Service

    firefox_options = Options()
    firefox_options.add_argument("--headless")

    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(
        service=s,
        options=firefox_options
    )


    driver.get("https://www.bloomberg.com/graphics/global-trade-indicators/")

    all_data = []

    data_list = driver.find_elements_by_css_selector('.container .indicator.svelte-1kp3mpm')

    for data in data_list:
        title = data.find_element_by_css_selector('h5>a').text
        recent_number = data.find_element_by_css_selector('g.bars rect:last-child').get_attribute('data-zscore')
        all_data.append([title, recent_number])

    df_panda = pd.DataFrame(all_data, columns=['Title', 'Recent Number'])
    df_panda.to_csv('all_data.csv', index=False)

    return send_from_directory(os.getcwd(), path='all_data.csv', as_attachment=True)