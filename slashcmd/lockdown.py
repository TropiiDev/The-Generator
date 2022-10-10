# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lockdown Online")

    @app_commands.command(name="lockdown", description="Lockdown the channel - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def lockdown(self, interaction: discord.Interaction):
        # make an if statement to lock the channel if not locked, and unlock the channel if locked
        if interaction.channel.overwrites_for(interaction.guild.default_role).send_messages == False:
            await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
            await interaction.response.send_message("Channel unlocked", ephemeral=True)
        else:
            await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
            await interaction.response.send_message("Channel locked down", ephemeral=True)

async def setup(bot):
    await bot.add_cog(lockdown(bot))