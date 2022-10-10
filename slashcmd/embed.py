# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Embed Online")

    @app_commands.command(name="embed", description="Send an embed - not hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def embed(self, interaction: discord.Interaction, title:str, description:str):
        em = discord.Embed(title=title, description=description, color=interaction.user.color)
        await interaction.response.send_message(embed=em)

async def setup(bot):
    await bot.add_cog(embed(bot))
    