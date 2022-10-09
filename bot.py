# pip install imports
import discord 
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio 

# sys imports
import os 
import logging
import logging.handlers

# check if discord.log exists if it does it deletes it than creates a new one
# if discord.log doesn't exist it creates a new one
# it is used to log errors
# it is also needed so the file doesnt get crammed with errors 
# its easier to understand when trying to look for errors in the code
if os.path.exists("discord.log"):
    os.remove("discord.log")
    open("discord.log", "x")
else:
    open("discord.log", "x")

# logging 
logger = logging.getLogger('discord')
logger.setLevel(logging.NOTSET)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# sys imports
import os


# startup stuff
load_dotenv()

async def load_extensions():
    for name in os.listdir('./slashcmd'):
        if name.endswith('.py'):
            await bot.load_extension(f'slashcmd.{name[:-3]}')

# load discord bot
guild = discord.Object(id=982466619240509471)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.synced = False
        
    async def setup_hook(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_ready(self):
        await tree.sync(guild=guild)
        self.synced = True

bot = MyBot()
tree = bot.tree

# start bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv("token"))
        await asyncio.sleep(0.1)
    await asyncio.sleep(0.1)

asyncio.run(main())