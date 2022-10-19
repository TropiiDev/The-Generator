import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid
import battleship as bs

class battleship2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Battleship Online")

    @app_commands.command(name="battleship", description="Play Battleship - Desktop Only")
    @app_commands.guilds(guildid.guilds)
    async def battleship(self, interaction: discord.Interaction, *, other: discord.Member):
        """Play a game of battleship with someone else"""
        if other.bot:
            return await interaction.response.send_message('You cannot play against a bot', ephemeral=True)

        prompt = bs.Prompt(interaction.user, other)
        prompt.message = await interaction.response.send_message(
            f'{other.mention} has been challenged to a game of Battleship by {interaction.user.mention}.\n'
            f'In order to accept, please press your button below to ready up.',
            view=prompt,
        )

async def setup(bot):
    await bot.add_cog(battleship2(bot))