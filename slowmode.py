# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid 

# sys import
import datetime

class slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slowmode Online")

    @app_commands.command(name="slowmode", description="Sets the channel slowmode")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, interaction: discord.Interaction, time:int):
        channel = interaction.channel
        if time > 21600:
            await interaction.response.send_message("You can only set slowmode to a maximum of 6 hours", ephemeral=True)
        else:
            await channel.edit(slowmode_delay=time)
            await interaction.response.send_message(f"A slowmode of {time} seconds has been set for {channel.mention}", ephemeral=True)
        if time < 0:
            await interaction.response.send_message("You can only set slowmode to a minimum of 0 seconds", ephemeral=True)

async def setup(bot):
    await bot.add_cog(slowmode(bot))