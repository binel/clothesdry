from flask import Flask, render_template, request 
import requests 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    forecast = get_forecast(0, 0)
    verdict = analyze(forecast)
    return render_template("index.html", verdict=verdict, forecast=forecast)

def get_forecast(lat, long):
    # dummy method to get the forecast for tonight - eventually will be real 
    return {
        "low_temp": 50.5,
        "dew_point": 41.5,
        "wind_speed": 9.1,
        "humidity": 0.19,
        "rain_chance": 0.15
    }

def analyze(forecast):
    if (forecast["rain_chance"] > 0):
        return "No - Chance of Rain"
    if (forecast["wind_speed"] > 20):
        return "No - High winds possible"
    if (forecast["low_temp"] - forecast["dew_point"] < 2):
        return "No - Dew likely"
    return "Yes"

if __name__ == "__main__":
    app.run(debug=True)
