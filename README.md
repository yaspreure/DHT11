# Flask-Based Temperature and Humidity Monitoring System

## Overview
This project is a Flask-based web application that reads temperature and humidity data from a DHT sensor connected to an Arduino. The data is collected via serial communication and displayed on a web interface.

## Features
- Reads temperature and humidity data using a DHT sensor.
- Displays real-time readings on a web interface.
- Uses Flask and Flask-Bootstrap for a responsive frontend.
- Collects data asynchronously using threading.
- Communicates with the sensor via serial (COM3 at 9600 baud rate).

## Technologies Used
- **Python (Flask, Flask-Bootstrap)** for the web application.
- **Arduino C++** for sensor data acquisition.
- **DHT sensor** for temperature and humidity readings.
- **Serial communication** for data transfer.

## Installation and Setup
### Prerequisites
- Python 3 installed
- Flask installed (`pip install flask flask-bootstrap`)
- Arduino with a DHT sensor

### Steps
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
2. **Connect the Hardware**
   - Attach the DHT sensor to pin 2 of the Arduino.
   - Connect the Arduino to your computer.
3. **Upload the Arduino Code**
   - Open the Arduino IDE.
   - Copy and paste the provided Arduino code.
   - Upload it to your Arduino board.
4. **Run the Flask Application**
   ```sh
   python app.py
   ```
5. **Access the Web Interface**
   - Open a browser and go to `http://127.0.0.1:5000/`

## Project Structure
```
├── app.py            # Flask application
├── templates/
│   ├── index.html    # Web interface template
├── static/
│   ├── styles.css    # CSS for styling (if applicable)
└── arduino_code.ino  # Arduino script for sensor data
```

## Arduino Code Breakdown
- Uses the `DHT.h` library to read temperature and humidity.
- Sends the data over serial communication at intervals.
- Sampling time is set to 3 minutes.

## Flask Application Breakdown
- Starts a background thread for continuous data collection.
- Reads sensor data via serial communication.
- Serves a web interface to display live readings.

## Future Improvements
- Store historical data in a database.
- Add data visualization using charts.
- Deploy the application on a cloud server.

## License
This project is open-source. Feel free to use and modify it!

