from discord.ext import commands
import discord
from discord import app_commands
from modals.feedback import Feedback
from settings import GUILD_ID


class ModalsCogs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de Modais prontos")

    @app_commands.guild_only()
    @app_commands.command(name="feedback", description="Submit feedback")
    async def feedback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Feedback())


async def setup(bot: commands.Bot):
    await bot.add_cog(ModalsCogs(bot), guilds=[discord.Object(GUILD_ID)])
