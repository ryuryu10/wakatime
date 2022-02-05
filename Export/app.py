from ossaudiodev import openmixer
from flask import Flask
from flask import render_template
from flask.helpers import total_seconds

import json
import pickle

app = Flask(__name__)

@app.route("/page3")
def main():

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
def main():
    with open('Database\days.pkl', 'rb') as f:
        days = pickle.load(f)
    with open('Database\seconds.pkl', 'rb') as f:
        seconds = pickle.load(f)

if __name__ == "__main__":
    app.run(debug=True)