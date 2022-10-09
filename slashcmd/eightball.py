# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# sys imports
import random

# local import
import guildid

class eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Eightball Online")

    @app_commands.command(name="eightball", description="Ask the magic eightball a question and it shall answer")
    @app_commands.guilds(guildid.guilds)
    async def eightball(self, interaction: discord.Interaction, question:str):
        responses = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes - definitely.',
            'You may rely on it.'
        ]
        await interaction.response.send_message(f"**Question**: {question}\nAnswer: {random.choice(responses)}")

async def setup(bot):
    await bot.add_cog(eightball(bot))