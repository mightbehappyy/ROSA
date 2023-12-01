from discord import app_commands
from discord.ext import commands
import discord
from settings import GUILD_ID
from ui.embebs.help_embed import HelpEmbed


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


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot), guilds=[discord.Object(GUILD_ID)])
