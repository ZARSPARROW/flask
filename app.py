from flask import Flask
import pandas as pd 
#calendartest.py imports
from env.Include.calendartest import umcdata
from env.Include.calendartest import holiday
from env.Include.calendartest import uvidata


app = Flask(__name__)
#calendartest.py
#umc function with using GET 
@app.route('/', methods=['GET'])
def umc():
    return 'hey everyone!' #  Function from your calendartest.py

@app.route('/umc', methods=['GET'])
def get_umc():
    return umcdata #  Function from your calendartest.py

#umch function with using GET 
@app.route('/umc/umch', methods=['GET'])
def get_umch():
    return holiday #  Function from your calendartest.py

#uvi function with using GET 
@app.route('/umc/umch/uvi', methods=['GET'])
def get_uvidata():
    return uvidata #  Function from your calendartest.py


if __name__ == '__main__':
    app.run(debug=True)