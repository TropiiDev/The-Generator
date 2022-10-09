# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping Online")

    @app_commands.command(name="ping", description="Sends the bots latency")
    @app_commands.guilds(guildid.guilds)
    async def self(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"**Pong!**\nLatency: {round(self.bot.latency * 1000)}ms")
    
async def setup(bot):
    await bot.add_cog(ping(bot))