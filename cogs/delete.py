import os

from discord import app_commands
from discord.ext import commands
import discord
from utils.functions.role_auth import check_for_role

GUILD_ID = int(os.getenv("GUILD_ID"))
AUTHORIZED_ROLE_ID = int(os.getenv("AUTHORIZED_ROLE_ID"))
class Delete(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comando deletar pronto")

    @app_commands.guild_only()
    @app_commands.command(name="deletar", description="Esse comando deleta mensagens")
    async def delete(self, interaction: discord.Interaction, number: int):
        if check_for_role(interaction, AUTHORIZED_ROLE_ID):
            if number > 100 or number < 1:
                await interaction.response.send_message(
                    "Só é possível deletar entre 1 e 100 mensagens"
                )
            else:
                await interaction.response.defer(thinking=True)
                await interaction.followup.send(
                    f":boom: Estou deletando {number} mensagens... :boom: "
                )
                await interaction.channel.purge(limit=number + 1)
        else:
            await interaction.response.send_message(
                "Você não tem permissão para usar esse comando"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Delete(bot), guilds=[discord.Object(GUILD_ID)])
