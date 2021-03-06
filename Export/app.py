
from flask import Flask
from flask import render_template

import json
import pickle

import os

from datetime import date
import datetime as dt

app = Flask(__name__)

@app.route('/page1')
def firhunc():

    datetime_date = date.today()
    x = dt.datetime.now()
    dateDict = {0: '월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
    dateDict[datetime_date.weekday()]

    return render_template(
        'page1.svg',
        month = x.month,
        day = x.day,
        letter = dateDict[datetime_date.weekday()]
    )

@app.route("/page3")
def firstfunc():

    with open('dump.json') as f:
        OPENED_json = json.load(f)

    sbar1 = OPENED_json['DATAS']['sidebar'][1].split(":")
    sbar2 = OPENED_json['DATAS']['sidebar'][2].split(":")
    sbar3 = OPENED_json['DATAS']['sidebar'][3].split(":")
    
    return render_template(
        'page2.svg', 
        sidebar1 = "0h 0m",
        sidebar2 = f'{sbar1[0]}h {sbar1[1]}m',
        sidebar3 = f'{sbar2[0]}h {sbar2[1]}m',
        sidebar4 = f'{sbar3[0]}h {sbar3[1]}m',
        date1 = OPENED_json['DATAS']['down_bar'][0],
        date2 = OPENED_json['DATAS']['down_bar'][1],
        date3 = OPENED_json['DATAS']['down_bar'][2],
        date4 = OPENED_json['DATAS']['down_bar'][3],
        date5 = OPENED_json['DATAS']['down_bar'][4],
        date6 = OPENED_json['DATAS']['down_bar'][5],
        date7 = OPENED_json['DATAS']['down_bar'][6],
        height1 = OPENED_json['DATAS']['graphs'][0],
        height2 = OPENED_json['DATAS']['graphs'][1],
        height3 = OPENED_json['DATAS']['graphs'][2],
        height4 = OPENED_json['DATAS']['graphs'][3],
        height5 = OPENED_json['DATAS']['graphs'][4],
        height6 = OPENED_json['DATAS']['graphs'][5],
        height7 = OPENED_json['DATAS']['graphs'][6],
        position1 = 567 - int(OPENED_json['DATAS']['graphs'][0]),
        position2 = 567 - int(OPENED_json['DATAS']['graphs'][1]),
        position3 = 567 - int(OPENED_json['DATAS']['graphs'][2]),
        position4 = 567 - int(OPENED_json['DATAS']['graphs'][3]),
        position5 = 567 - int(OPENED_json['DATAS']['graphs'][4]),
        position6 = 567 - int(OPENED_json['DATAS']['graphs'][5]),
        position7 = 567 - int(OPENED_json['DATAS']['graphs'][6])
        )

@app.route('/page2')
def secondfunc():
    total_sums = 0

    sums = 0

    with open('Database\days.pkl', 'rb') as f:
        days = pickle.load(f)
    with open('Database\seconds.pkl', 'rb') as f:
        seconds = pickle.load(f)
    print(days, seconds)

    for a in seconds:
        sums += a

    file_list = os.listdir('./Database/Archive')
    for file in file_list:
        f = open(f'Database\Archive\{file}', "r")
        rd = f.read()
        total_sums += int(rd)

    print ("file_list: {}".format(file_list))   

    return render_template(
        'page3.svg',
        today_time = seconds[-1],
        last7days_time = sums,
        total_time = total_sums
    )

if __name__ == "__main__":
    app.run(debug=True)