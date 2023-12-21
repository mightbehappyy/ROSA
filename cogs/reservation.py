from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
import discord
from utils.lists.settings import GUILD_ID
from ui.embebs.week_events_embed import WeekEventsEmbed


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
        await interaction.response.send_message(f"Já te mando as reservas do {lab.name} :smile:", ephemeral=True)
        await interaction.followup.send(embed=WeekEventsEmbed(lab.value, lab.name).get_week_events_embed(), ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Reservation(bot), guilds=[discord.Object(GUILD_ID)])
