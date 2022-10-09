import discord
from discord import app_commands
from discord.ext import commands

import guildid

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Purge Online")

    @app_commands.command(name="purge", description="Bulk deletes a number of messages")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, interaction: discord.Interaction, amount:int):
        if amount > 100:
            await interaction.response.send_message("You can only delete up to 100 messages at a time")
        else:
            await interaction.response.send_message(f"Deleted {amount} messages", ephemeral=True)
            await interaction.channel.purge(limit=amount)

async def setup(bot):
    await bot.add_cog(purge(bot))