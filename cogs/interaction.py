from discord import app_commands
from discord.ext import commands
import discord
from settings import PPC_LINK, GUILD_ID


class Interaction(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")

    @app_commands.command(name="oi", description="Say hello!")
    async def presentation(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Oi! Eu sou a ROSA (Reserve Online Sua Aula) e estou aqui para te ajudar a reservar os laboratórios de informática da UPE campus Garanhuns"
        )

    @app_commands.command(
        name="ppc",
        description="Retorna o PPC do curso de Engenharia de Software da UPE campus Garanhuns",
    )
    async def ppc(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Aqui está o PPC do curso de Engenharia de Software da UPE campus Garanhuns"
        )
        await interaction.followup.send(PPC_LINK)


async def setup(bot: commands.Bot):
    await bot.add_cog(Interaction(bot), guilds=[discord.Object(GUILD_ID)])
