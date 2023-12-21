import discord
from src.apis.services.weather_service import WeatherService
from src.utils.lists.weather_stats_dict import get_weather_stats_dict
from src.utils.functions.translate_day import translate

class WeatherEmbeds:

    def __init__(self, city):
        self.weather_service = WeatherService(city)

    def get_graph_embed(self):
        weather_graph = self.weather_service.get_weather_graph()
        embed = discord.Embed(
            title=f"Tempo em {weather_graph['name']} - {weather_graph['region']} ({weather_graph['country']})", color=0xFFFFFF
        )

        embed.set_image(url=weather_graph['url'])
        return embed

    def get_weather_stats_embeb(self):
        info = self.weather_service.get_weather_stats()
        field_dict = get_weather_stats_dict(info)
        embed = discord.Embed(
            title=f"Tempo em {info['name']}, {info['region']} ({info['country']})",
            url="https://portal.inmet.gov.br/",
            color=0xFFFFFF,
        )

        embed.set_thumbnail(url=f"https:{info['icon']}")

        for field in field_dict:
            embed.add_field(
                name=field_dict[field][0], value=field_dict[field][1], inline=True
            )
        embed.set_footer(text="Fetched from https://www.weatherapi.com/")

        return embed
