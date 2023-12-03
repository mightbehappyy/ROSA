from discord.ext import commands
import discord
from settings import AUTHORIZED_ROLE_ID, GUILD_ID
from discord import app_commands
import apis.calendar_controller as CalendarAPI
from utils.functions.role_auth import check_for_role
from ui.embebs.reservation import ReservationEmbeds
from discord.app_commands import Choice
from ui.modals.reservation_modal import ReservationModal


class Reservations(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.embeds = ReservationEmbeds()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comandos de reservas prontos")

    @commands.guild_only()
    @app_commands.command(name="reservar", description="Reserve um horário")
    @app_commands.choices(
        lab=[
            Choice(name="Laboratório Windows", value=1),
            Choice(name="Laboratório Linux", value=2),
        ]
    )
    async def reserva(
        self, interaction: discord.Interaction, lab: discord.app_commands.Choice[int]
    ):
        try:
            # if check_for_role(interaction, AUTHORIZED_ROLE_ID):
            await interaction.response.send_modal(ReservationModal())
        # else:
        # await interaction.response.send_message(
        #     "Você não tem permissão para usar esse comando", ephemeral=True
        # )
        except Exception as e:
            print(e)

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
        await interaction.response.defer(ephemeral=True)
        embed = self.embeds.get_week_events_embed(
            CalendarAPI.check_calendar(lab.value), lab.value
        )
        await interaction.followup.send(embed=embed)

    @app_commands.command(
        name="checar_reservas_futuras",
        description="Checa reserva futuras em até 10 semanas",
    )
    @app_commands.choices(
        lab=[
            Choice(name="Laboratório Windows", value=1),
            Choice(name="Laboratório Linux", value=2),
        ],
        semanas=[
            Choice(name="1 semana", value=1),
            Choice(name="2 semana", value=2),
            Choice(name="3 semana", value=3),
            Choice(name="4 semana", value=4),
            Choice(name="5 semana", value=5),
            Choice(name="6 semana", value=6),
            Choice(name="7 semana", value=7),
            Choice(name="8 semana", value=8),
            Choice(name="9 semana", value=9),
            Choice(name="10 semana", value=10),
        ],
    )
    async def checar_reserva_futura(
        self,
        interaction: discord.Interaction,
        lab: discord.app_commands.Choice[int],
        semanas: discord.app_commands.Choice[int],
    ):
        await interaction.response.defer(ephemeral=True)
        embed = self.embeds.get_week_events_embed(
            CalendarAPI.get_future_weeks_schedule(lab.value, semanas.value), lab.value
        )
        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Reservations(bot), guilds=[discord.Object(GUILD_ID)])
