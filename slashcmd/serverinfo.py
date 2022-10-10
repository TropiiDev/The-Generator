# pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Serverinfo Online")

    @app_commands.command(name="serverinfo", description="Get info about the server - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def serverinfo(self, interaction: discord.Interaction):
        role_count = len(interaction.guild.roles)

        em = discord.Embed(color = interaction.user.color)
        em.add_field(name="Server Name", value=f"{interaction.guild.name}", inline=False)
        em.add_field(name="Member Count", value=f"{interaction.guild.member_count}", inline=False)
        em.add_field(name="Verify Level", value=f"{interaction.guild.verification_level}", inline=False)
        em.add_field(name="Highest Role", value=f"{interaction.guild.roles[-2]}", inline=False)
        em.add_field(name="Number Of Roles", value=f"{role_count}", inline=False)
        em.add_field(name="Guild ID", value=f"{interaction.guild.id}", inline=False)

        await interaction.response.send_message(embed=em, ephemeral=True)

async def setup(bot):
    await bot.add_cog(serverinfo(bot))