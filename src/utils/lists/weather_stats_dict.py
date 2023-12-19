def get_weather_stats_dict(info: dict) -> dict:
    field_dict = {
        "temperature": [
            ":thermometer: Temperatura",
            f"{info['temperature']}°C",
        ],
        "humidity": [
            ":droplet: Umidade",
            f"{info['humidity']} %",
        ],
        "cloud": [
            ":cloud: Cobertura",
            f"{info['cloud']} %",
        ],
        "wind": [
            ":dash: Velocidade do vento",
            f"{info['windSpeed']}km/h",
        ],
        "feels_like": [
            ":person_getting_massage: Sensação termica",
            f"{info['feelsLike']}°C",
        ],
        "time": [
            ":alarm_clock: Horário",
            f"{info['localTime']}",
        ],
    }
    return field_dict
