from ast import Import
from logging import raiseExceptions
from multiprocessing.pool import INIT
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, timedelta
from selenium import webdriver

from datetime import time, date, timedelta
import datetime
import os


from function import image1, image2, image3

_URL = "http://wakatime.com/dashboard"
_AUTOLOGIN = True
_DEBUG = True

#MTY : 567
#ㄴ H : 0

Last_7_Days_Date_List = []
Last_7_Days_Time_List = []
temp = []
Last_7_Days_Second_List = []

today = date.today()
for numbers in range(6,0,-1):
    Last_7_Days_Date_List.append(date.today() - timedelta(numbers))
Last_7_Days_Date_List.append(date.today())

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome("chromedriver.exe")
driver.get(_URL)
driver.implicitly_wait(10)
print("Login wait")
if _AUTOLOGIN == True:
    import json
    with open('config.json') as f:
        login_data = json.load(f)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/a').click()
    WebDriverWait(driver,timeout=999).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[3]')))
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(login_data['id'])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(login_data['pw'])
    driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/div/input[12]').click()
    pass
p_tag = WebDriverWait(driver,timeout=999).until(EC.presence_of_element_located((By.CLASS_NAME, "bb-chart")))
print("Login End")
for day in Last_7_Days_Date_List:
    driver.get(f'http://wakatime.com/dashboard/day?date={day}')
    driver.implicitly_wait(10)
    times = driver.find_element_by_xpath('//*[@id="total-logged-time"]/b').text
    Last_7_Days_Time_List.append(times)
driver.quit()

os.system('cls')
for times in Last_7_Days_Time_List:
    splited = times.split(" ")
    temp_seconds = 0
    if len(splited) == 2:
        temp_seconds = int(splited[0]) * 60
        Last_7_Days_Second_List.append(temp_seconds)
        print(datetime.timedelta(seconds=int(temp_seconds)))

    elif len(splited) == 4:
        temp_seconds = int(splited[0]) * 3600
        temp_seconds += int(splited[2]) * 60
        Last_7_Days_Second_List.append(temp_seconds)
        print(datetime.timedelta(seconds=int(temp_seconds)))

    else:
        print("ERROR", splited,len(splited))

image2.maker(Last_7_Days_Second_List, Last_7_Days_Date_List)