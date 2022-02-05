from flask import Flask
from flask import render_template
from flask.helpers import total_seconds

import json

app = Flask(__name__)

@app.route("/")
def main():
        
    return render_template(
        'page2.svg', 
        tempdata = "123"
        )

if __name__ == "__main__":
    app.run(debug=True)