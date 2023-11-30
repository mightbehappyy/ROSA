from discord.ext import commands
import discord
from discord import app_commands
from apis.GraphAPI import get_weather_graph, get_weather_stats
from embebs.weather_graph_embed import WeatherEmbeds
from settings import GUILD_ID


class Weather(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.weather_embed = WeatherEmbeds()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de tempo prontos")

    @app_commands.command(
        name="graficotempo",
        description="Mostra a progressão do tempo durante o dia de uma cidade",
    )
    async def weather_graph(self, interaction: discord.Interaction, cidade: str):
        await interaction.response.defer(thinking=True)
        city_name, region_name, image_url = get_weather_graph(cidade)
        embed = self.weather_embed.get_graph_embed(city_name, region_name, image_url)
        await interaction.followup.send(embed=embed)

    @app_commands.command(
        name="tempo", description="Mostra o tempo em uma cidade no momento"
    )
    async def time(self, interaction: discord.Interaction, cidade: str):
        await interaction.response.defer(thinking=True)
        info = get_weather_stats(cidade)
        embed = self.weather_embed.get_weather_stats_embeb(info)
        await interaction.followup.send(embed=embed)

    @time.error
    @weather_graph.error
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.followup.send(
            "Não consegui encontrar essa cidade. Desculpe! :cry:"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Weather(bot), guilds=[discord.Object(GUILD_ID)])
