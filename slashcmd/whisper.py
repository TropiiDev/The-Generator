# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class whisper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Whisper Online")

    @app_commands.command(name="whisper", description="Whisper a user - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def whisper(self, interaction: discord.Interaction, user: discord.Member, *, message:str):
        await user.send(message)
        await interaction.response.send_message(f"Sent message to {user.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(whisper(bot))