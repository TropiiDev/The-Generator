# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Avatar Online")

    @app_commands.command(name="avatar", description="Get a users avatar")
    @app_commands.guilds(guildid.guilds)
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user
            embed = discord.Embed(title=f"{member.name}'s avatar")
            embed.set_image(url=member.avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title=f"{member.name}'s avatar")
            embed.set_image(url=member.avatar.url)
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(avatar(bot))