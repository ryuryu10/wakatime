from flask import Flask
from flask import render_template
from flask.helpers import total_seconds

import json

app = Flask(__name__)

@app.route("/")
def main():

    with open('dump.json') as f:
        OPENED_json = json.load(f)
    
    print(OPENED_json['DUMP_version'])
    print(OPENED_json['DATAS']['sidebar'])
    print(OPENED_json['DATAS']['graphs'])
    print(OPENED_json['DATAS']['down_bar'])

    sbar1 = OPENED_json['DATAS']['sidebar'][1].split(":")
    sbar2 = OPENED_json['DATAS']['sidebar'][2].split(":")
    sbar3 = OPENED_json['DATAS']['sidebar'][3].split(":")
    
        
    return render_template(
        'page2.svg', 
        sidebar1 = "0h 0m",
        sidebar2 = f'{sbar1[0]}h {sbar1[1]}m',
        sidebar3 = f'{sbar2[0]}h {sbar2[1]}m',
        sidebar4 = f'{sbar3[0]}h {sbar3[1]}m',
        
        )

if __name__ == "__main__":
    app.run(debug=True)