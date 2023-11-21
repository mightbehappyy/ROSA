from quickchart import QuickChart
import requests
from settings import WEATHER_API_TOKEN

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.device_pixel_ratio = 2.0


def get_weather_graph(city):
    time_stamps = []
    day_temps = []
    day_humidity = []
    day_termic_sensation = []
    day_avg_temp = []
    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_TOKEN}&q={city}&days=1&aqi=no&alerts=no"

    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    city_api = data["location"]["name"]
    region_api = data["location"]["region"]

    avg_temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]

    hourly_temperatures = [
        hour["temp_c"] for hour in data["forecast"]["forecastday"][0]["hour"]
    ]
    hourly_humidity = [
        hour["humidity"] for hour in data["forecast"]["forecastday"][0]["hour"]
    ]
    feels_like = [
        hour["feelslike_c"] for hour in data["forecast"]["forecastday"][0]["hour"]
    ]

    for idx, (temp_c, humidity, feelslike) in enumerate(
        zip(hourly_temperatures, hourly_humidity, feels_like)
    ):
        day_avg_temp.append(avg_temp)
        time_stamps.append(str(f"{idx}:00"))
        day_temps.append(temp_c)
        day_humidity.append(humidity)
        day_termic_sensation.append(feelslike)

    qc.config = {
        "type": "line",
        "data": {
            "labels": time_stamps,
            "datasets": [
                {"label": "Temperatura", "data": day_temps, "fill": False},
                {"label": "Temperatura Média", "data": day_avg_temp, "fill": False},
                {"label": "Umidade", "data": day_humidity, "fill": False},
                {
                    "label": "Sensação Termica",
                    "data": day_termic_sensation,
                    "fill": False,
                },
            ],
        },
    }

    return city_api, region_api, qc.get_url()


def get_weather_stats(city):
    api_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_TOKEN}&q={city}&aqi=no"
    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    current = data["current"]
    location = data["location"]

    info_dict = {
        "city_name": location["name"],
        "time": location["localtime"],
        "temperature_celsius": current["temp_c"],
        "humidity": current["humidity"],
        "feels_like": current["feelslike_c"],
        "cloud": current["cloud"],
        "wind_kph": current["wind_kph"],
        "icon": current["condition"]["icon"],
    }

    return info_dict
