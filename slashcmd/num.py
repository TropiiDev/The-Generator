# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class num(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Num Online")

    @app_commands.command(name="num", description="Checks if a number is even or odd - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def num(self, interaction: discord.Interaction, number:int):
        if number % 2 == 0:
            await interaction.response.send_message(f"{number} is even", ephemeral=True)
        else:
            await interaction.response.send_message(f"{number} is odd", ephemeral=True)

async def setup(bot):
    await bot.add_cog(num(bot))