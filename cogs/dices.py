from discord.ext import commands
import discord
from discord import app_commands
from random import randint
from settings import GUILD_ID


class Dices(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de dados prontos")

    @app_commands.command(
        name="d20", description="Role um d20 para descobrir seu destino"
    )
    async def d20(self, interaction: discord.Interaction):
        d20_value = randint(1, 20)
        await interaction.response.send_message(f"`{d20_value}` ⟵ Total")


async def setup(bot: commands.Bot):
    await bot.add_cog(Dices(bot), guilds=[discord.Object(GUILD_ID)])
