# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Nick Online")

    @app_commands.command(name="nick", description="Change your nickname - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def nick(self, interaction: discord.Interaction, *, nickname:str):
        await interaction.user.edit(nick=nickname)
        await interaction.response.send_message(f"Changed nickname to {nickname}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(nick(bot))