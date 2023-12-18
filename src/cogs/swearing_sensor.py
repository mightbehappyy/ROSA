from discord.ext import commands
import discord
from src.utils.lists.settings import GUILD_ID


class SwearingSensor(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Sensor de xingamentos pronto")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        with open("words.txt", "r") as file:
            prohibited_words = file.read().splitlines()

        if any(word.lower() in message.content.lower() for word in prohibited_words):
            author_id = message.author.id
            await message.delete()
            await message.channel.send(
                f"<@{author_id}> Talvez não seja tão legal falar isso :face_with_diagonal_mouth:"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(SwearingSensor(bot), guilds=[discord.Object(GUILD_ID)])
