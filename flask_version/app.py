from flask import Flask,render_template,redirect,url_for,request
import requests

# Wsgi object instantiation
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods = ["POST","GET"])
def search():
    if request.method == "POST":
        city = request.form["city"] 
        return redirect(url_for('fetch_weather_data',city = city))
    

@app.route("/fetch_weather/<string:city>")
def fetch_weather_data(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    apikey = open("api_key.txt","r").read()
    URL = BASE_URL + "q=" + city +"&appid=" + apikey

    try:
        response = requests.get(URL)

        # check if the json file was sucessfully retrived 
        if response.status_code == 200:
            # Parsing the json file
            weather_data = response.json()
            weather_data_info = { "City" : weather_data["name"],
                    "Condition" : weather_data["sys"]["country"],
                    "Temprature": weather_data["main"]["temp"],
                    "Feels like ": weather_data["main"]["feels_like"],
                    "Humidity": weather_data["main"]["humidity"],
                    "Wind Speed": weather_data["wind"]["speed"],
                    "Sunrise": weather_data["sys"]["sunrise"],
                    "Sunset": weather_data["sys"]["sunset"],
                     }
            return render_template("weather.html", weather = weather_data_info)
        else:
           return { "error": "City not found" }

    except requests.exceptions.RequestException as e:
        return f"Error occured{e}"

if __name__ == "__main__":
    app.run(debug=True)