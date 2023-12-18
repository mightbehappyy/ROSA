from discord import app_commands
from discord.ext import commands
import discord
from src.utils.lists.settings import GUILD_ID
from src.ui.embebs.help_embed import HelpEmbed
from src.ui.modals.reservation_modal import ReservationModal

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comando ajuda pronto")

    @app_commands.guild_only()
    @app_commands.command(
        name="ajuda", description="Retorna a lista de comandos da rosa"
    )
    async def help(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            ephemeral=True, embed=HelpEmbed.create_help_embed()
        )

    @app_commands.command(
            name="reservar", description="Retorna a lista de comandos da rosa")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ReservationModal())


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot), guilds=[discord.Object(GUILD_ID)])
