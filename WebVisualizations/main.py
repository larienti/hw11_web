
from flask import Flask, jsonify, render_template


app = Flask(__name__)


#routes

@app.route("/")
def landing():
    #"link to other pages"
    return render_template('landing.html')

@app.route("/temperature/")
def temperature():
    return render_template('temperature.html')

@app.route("/humidity/")
def humidity():
    return render_template('humidity.html')

@app.route("/wind/")
def wind():
    return render_template('wind.html')

@app.route("/cloudiness/")
def cloudiness():
    return render_template('cloudiness.html')

@app.route("/comparisons/")
def comparisons():
    return render_template('comparisons.html')

@app.route("/index/")
def dataindex():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')