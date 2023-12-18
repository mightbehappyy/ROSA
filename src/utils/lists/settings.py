import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_TOKEN = os.getenv("WEATHER_API_TOKEN")
AUTHORIZED_ROLE_ID = int(os.getenv("AUTHORIZED_ROLE_ID"))
PPC_LINK = os.getenv("PPC_LINK")
GUILD_ID = int(os.getenv("GUILD_ID"))
APPLICATION_ID = int(os.getenv("APPLICATION_ID"))
LAB_WINDOWS_ID = os.getenv("LAB_WINDOWS_ID")
LAB_LINUX_ID = os.getenv("LAB_LINUX_ID")
