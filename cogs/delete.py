from discord import app_commands
from discord.ext import commands
import discord
from settings import AUTHORIZED_ROLE_ID, GUILD_ID
from utils import check_for_role


class Delete(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comando deletar pronto")

    @app_commands.guild_only()
    @app_commands.command(name="deletar", description="Esse comando deleta mensagens")
    async def deletar(self, interaction: discord.Interaction, number: int):
        if check_for_role(interaction, AUTHORIZED_ROLE_ID) == True:
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
