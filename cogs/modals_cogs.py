from discord.ext import commands
import discord
from discord import app_commands
from ui.modals.reservation_modal import ReservationModal
from settings import GUILD_ID


class ModalsCogs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de Modais prontos")


async def setup(bot: commands.Bot):
    await bot.add_cog(ModalsCogs(bot), guilds=[discord.Object(GUILD_ID)])
