from discord.ext import commands
import discord
from settings import AUTHORIZED_ROLE_ID, GUILD_ID
from discord import app_commands
import CalendarAPI
from utils import check_for_role
from embebs.reservation import ReservationEmbeds
from discord.app_commands import Choice


class Reservations(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.embeds = ReservationEmbeds()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de reservas prontos")

    @commands.guild_only()
    @app_commands.command(name="reservar", description="Reserve um horário")
    async def reserva(
        self,
        interaction: discord.Interaction,
        summary: str,
        starttime: str,
        endtime: str,
        date: str,
    ):
        CalendarAPI.post_event(summary, starttime, endtime, date)

    @app_commands.command(
        name="checar_reserva", description="Checa o calendário para futuros eventos"
    )
    @app_commands.describe(lab="O laboratório que você deseja visualizar o horário")
    @app_commands.choices(
        lab=[
            Choice(name="Laboratório Windows", value=1),
            Choice(name="Laboratório Linux", value=2),
        ]
    )
    async def checar_reserva(
        self, interaction: discord.Interaction, lab: discord.app_commands.Choice[int]
    ):
        if check_for_role(interaction, AUTHORIZED_ROLE_ID) == False:
            await interaction.response.send_message(
                "Você não tem permissão para usar esse comando"
            )
        else:
            await interaction.response.defer(ephemeral=True)
            embed = self.embeds.get_week_events_embed(
                CalendarAPI.check_calendar(lab.value), lab.value
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Reservations(bot), guilds=[discord.Object(GUILD_ID)])
