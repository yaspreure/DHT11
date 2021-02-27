from flask import Flask, jsonify, render_template, url_for, request
import threading, queue
import serial
from datetime import datetime
from flask_bootstrap import Bootstrap

ser = serial.Serial("COM3",9600)
app = Flask(__name__)
Bootstrap(app)
q = queue.Queue()


temperature = []
humidity = []
time_ax = []

def data_collection():

        temperature_r = ser.read(5).decode('utf-8')
        humidity_r = ser.read(5).decode('utf-8')
        time_of_reading = datetime.now()


        print(temperature_r)
        print(humidity_r)
        print(time_of_reading)

        q.put(temperature_r)
        q.put(humidity_r)
        q.put(time_of_reading.strftime("%H:%M"))

@app.route("/")
def index():
    return render_template("index.html", temperature=ser.read(5).decode('utf-8'), humidity=ser.read(5).decode('utf-8'), time_of_reading=datetime.now())
    return jsonify(results=[temperature, humidity, time_ax])

if __name__ == '__main__':
    x = threading.Thread(target=data_collection)
    x.start()
    app.run(host = '127.0.0.1', port = 5000)
