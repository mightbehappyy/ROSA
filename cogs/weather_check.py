from discord import app_commands
from discord.ext import commands
import discord

from apis.services.weather_service import WeatherService
from ui.embebs.weather_graph_embed import WeatherEmbeds
from utils.lists.settings import GUILD_ID


class WeatherCheck(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Checagem de clima pronto")

    @app_commands.guild_only()
    @app_commands.command(
        name="tempo", description="Retorna os dados do clima no momento"
    )
    async def get_weather_stats(self, interaction: discord.Interaction, city: str):
        weather_stats_embed = WeatherEmbeds(city)
        await interaction.response.defer()
        await interaction.followup.send(ephemeral=True, embed=weather_stats_embed.get_weather_stats_embeb())

    @app_commands.guild_only()
    @app_commands.command(
        name="tempo_grafico", description="Retorna os dados um grafico do tempo ao longo do dia"
    )
    async def get_weather_graph(self, interaction: discord.Interaction, city: str):
        weather_stats_embed = WeatherEmbeds(city)
        await interaction.response.defer()
        await interaction.followup.send(ephemeral=True, embed=weather_stats_embed.get_graph_embed())


async def setup(bot: commands.Bot):
    await bot.add_cog(WeatherCheck(bot), guilds=[discord.Object(GUILD_ID)])
