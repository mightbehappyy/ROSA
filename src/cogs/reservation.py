from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
import discord
from src.utils.lists.settings import GUILD_ID
from src.ui.embebs.help_embed import HelpEmbed
from src.apis.controllers.calendar_controller import CalendarController
from src.ui.embebs.week_events_embed import WeekEventsEmbed


class Reservation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comando de reservas pronto")

    @app_commands.guild_only()
    @app_commands.command(
        name="checar_reserva", description="Retorna a lista de eventos nos laboratórios"
    )
    @app_commands.choices(
        lab=[
            Choice(name="Laboratório Windows", value="1"),
            Choice(name="Laboratório Linux", value="2"),
        ]
    )
    async def check_reservation(self, interaction: discord.Interaction, lab: discord.app_commands.Choice[str]):
        await interaction.response.defer()
        await interaction.followup.send(
            ephemeral=True, embed=WeekEventsEmbed(lab.value).get_week_events_embed()
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Reservation(bot), guilds=[discord.Object(GUILD_ID)])
