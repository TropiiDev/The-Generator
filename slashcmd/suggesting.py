# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid


class suggesting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Suggesting Online")

    @app_commands.command(name="suggest", description="Suggest a command to the bot")
    @app_commands.guilds(guildid.guilds)
    async def suggest(self, interaction: discord.Interaction, *, suggestion:str):
        owner = self.bot.get_user(875604204889202698)
        await owner.send(f"{interaction.user} has suggested {suggestion}")
        await interaction.response.send_message("Your suggestion has been sent to the bot owner. Thanks for your suggestion!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(suggesting(bot))