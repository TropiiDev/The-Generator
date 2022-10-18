# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Support Online")

    @app_commands.command(name="support", description="Support Server")
    @app_commands.guilds(guildid.guilds)
    async def support(self, interaction: discord.Interaction):
        em = discord.Embed(title="Support", description=None, color = interaction.user.color)
        em.add_field(name="Support Server", value="https://discord.gg/mu4XBRNkBj", inline=False)
        em.add_field(name="Don't want to join the server?", value="Thats okay use command `/suggest` to suggest a feature or report a bug.")
        em.set_footer(text="Created by The Generator")

        await interaction.response.send_message(embed=em, ephemeral=True)

async def setup(bot):
    await bot.add_cog(support(bot))