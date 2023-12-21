import discord
from utils.lists import commands


class HelpEmbed:
    @staticmethod
    def create_help_embed():
        embed = discord.Embed(
            title="Lista de Comandos :technologist: ",
            description="Aqui estão os comandos disponíveis:",
            color=0x7289DA,
        )

        for command, description in commands:
            embed.add_field(name=command, value=description, inline=False)

        return embed
