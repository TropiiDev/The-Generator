# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class repeat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Repeat Online")

    @app_commands.command(name="repeat", description="Repeat after what the player says")
    @app_commands.guilds(guildid.guilds)
    async def repeat(self, interaction: discord.Interaction, *, text:str):
        await interaction.response.send_message(text, ephemeral=True)

async def setup(bot):
    await bot.add_cog(repeat(bot))