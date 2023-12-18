import discord
from discord.ext import commands
from src.utils.lists.settings import GUILD_ID, APPLICATION_ID, BOT_TOKEN
from src.utils.lists.coglist import cogs_list

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "production" bot
TEST_GUILD = discord.Object(GUILD_ID)


class MyClient(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id=APPLICATION_ID,
        )

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def setup_hook(self):
        for cog in cogs_list:
            await self.load_extension(cog)

        await self.tree.sync(guild=TEST_GUILD)


client = MyClient()


client.run(BOT_TOKEN)
