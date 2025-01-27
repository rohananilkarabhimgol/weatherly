Weather App

This repository contains two versions of a weather application: a terminal-based CLI version and a Flask-based web application. The app fetches real-time weather data from the OpenWeather API and displays key weather information such as temperature, humidity, wind speed, and more.

weather-app/
|
├── README.md                # Project documentation
├── terminal_version/        # Terminal-based weather app
│   ├── weather_cli.py       # Script for CLI-based weather data fetch
│   └── requirements.txt     # Dependencies for terminal version
│
├── flask_version/           # Flask-based weather web app
│   ├── app.py               # Flask app for fetching and displaying weather
│   ├── templates/           # HTML templates
│   │   ├── index.html       # Welcome page
│   │   ├── weather.html     # Weather result page
│   ├── static/              # Static files
│   │   └── css/style.css    # CSS styles for the web app
│   └── requirements.txt     # Dependencies for Flask version
│
├── api_key.txt              # File to store your OpenWeather API key (excluded from version control)
└── __pycache__/             # Compiled Python files (ignore this folder)

Prerequisites

API Key: Obtain an API key from OpenWeather API.

Python: Ensure Python 3.7 or higher is installed.

pip: Python package manager for installing dependencies.

Setup

1. Clone the Repository

git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Add Your API Key

Create a file named api_key.txt in the root folder and paste your OpenWeather API key inside it:
# Example of api_key.txt
YOUR_API_KEY_HERE

Running the Terminal Version

Steps:

1.Navigate to the terminal_version/ folder:
cd terminal_version

2.Install the required dependencies:
pip install -r requirements.txt

3.Run the script:
python weather_cli.py

4.Enter the city name when prompted to fetch weather information.

Running the Flask Version

Steps:

1.Navigate to the flask_version/ folder:
cd flask_version

2.Install the required dependencies:
pip install -r requirements.txt

3.Run the Flask application:
python app.py

4.Open your web browser and navigate to:
http://127.0.0.1:5000/

5.Enter the city name in the input box and view the weather information.


Features

Terminal Version:

Simple, text-based interface.

Fetches and displays weather data in the terminal.

Flask Version:

User-friendly web interface.

Real-time weather data display for any city.

Styled using CSS.