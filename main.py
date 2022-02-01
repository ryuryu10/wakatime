from logging import raiseExceptions
from multiprocessing.pool import INIT
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, time, timedelta
from selenium import webdriver

import json

_URL = "http://wakatime.com/dashboard"

week = []
week_time = []
today = date.today()
print(type(date.today() - timedelta(1)))
for numbers in range(6,0,-1):
    week.append(date.today() - timedelta(numbers))
week.append(date.today())


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome("chromedriver.exe")
driver.get(_URL)
driver.implicitly_wait(10)
print("Login wait")
p_tag = WebDriverWait(driver,timeout=999).until(EC.presence_of_element_located((By.CLASS_NAME, "bb-chart")))
print("Login End")
for day in week:
    driver.get(f'http://wakatime.com/dashboard/day?date={day}')
    driver.implicitly_wait(10)
    times = driver.find_element_by_xpath('//*[@id="total-logged-time"]/b').text
    week_time.append(times)
driver.quit()
for times in week_time:
    splited = times.split(" ")
    if len(splited) == "2":
        #mins data
        CODE_hour = 0
        CODE_min = splited[0]
    elif len(splited) == "4":
        #hours, mins data
        CODE_hour = splited[0]
        CODE_min = splited[2]
    else:
        raiseExceptions("None data.")
    print(splited)
f = open('./dump.json')
f.write(CODE_hour, CODE_min)
f.close()