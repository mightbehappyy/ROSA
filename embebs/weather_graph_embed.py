import discord


class WeatherEmbeds:
    def get_graph_embed(self, city_name, region_name, image_url):
        embed = discord.Embed(
            title=f"Tempo em {city_name} - {region_name}", color=0xFFFFFF
        )
        embed.set_image(url=image_url)
        return embed

    def get_weather_stats_embeb(self, info):
        embed = discord.Embed(
            title=f"Tempo em {info['city_name']}",
            url="https://portal.inmet.gov.br/",
            color=0xFFFFFF,
        )

        embed.set_thumbnail(url=f"https:{info['icon']}")

        field_dict = {
            "temperature": [
                ":thermometer: Temperatura",
                f"{info['temperature_celsius']}°C",
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
                f"{info['wind_kph']}km/h",
            ],
            "feels_like": [
                ":person_getting_massage: Sensação termica",
                f"{info['feels_like']}°C",
            ],
            "time": [
                ":alarm_clock: Horário",
                f"{info['time']}",
            ],
        }

        for field in field_dict:
            embed.add_field(
                name=field_dict[field][0], value=field_dict[field][1], inline=True
            )
        embed.set_footer(text="Fetched from https://www.weatherapi.com/")

        return embed
