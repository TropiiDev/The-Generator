# pip install imports
import discord
from discord import app_commands
from discord.ext import commands
import datetime

# local imports
import guildid

class timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Timeout Online")
    
    @app_commands.command(name="timeout", description="Timeout a user")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(administrator=True)
    async def timeout(self, interaction: discord.Interaction, member:discord.Member, time:int, reason:str = None):
        await member.timeout(datetime.timedelta(minutes=time), reason=reason)
        await interaction.response.send_message(f"{member.mention} has been timed out for {reason}", ephemeral=True)
        
    @app_commands.command(name="removetimeout", description="Removes the users timeout")
    @app_commands.guilds(guildid.guilds)
    async def removetimeout(self, interaction: discord.Interaction, member: discord.Member, reason:str = None):
        await member.timeout(None)
        await interaction.response.send_message(f"{member.mention} has been untimed out for {reason}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(timeout(bot))