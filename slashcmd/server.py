#pip install imports
import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Server Online")

    @app_commands.command(name="rules", description="Server Info")
    @app_commands.guilds(guildid.guilds)
    @app_commands.checks.has_permissions(administrator=True)
    async def rules(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user
        else: 
            member = member
        em = discord.Embed(title=None, description=f"{member.mention} here are the rules", color=0x00ff00)
        em.add_field(name="Rule 1", value="Treat everyone with respect. Absolutely no harassment, witch hunting, sexism, racism, or hate speech will be tolerated.", inline=False)
        em.add_field(name="Rule 2", value="No spam or self-promotion (server invites, advertisements, etc) without permission from a staff member. This includes DMing fellow members.", inline=False)
        em.add_field(name="Rule 3", value="No NSFW or obscene content. This includes text, images, or links featuring nudity, sex, hard violence, or other graphically disturbing content.", inline=False)
        em.add_field(name="Rule 4", value="Keep it calm around here nobody wants to be in a server that is all around bad energy or just full of negativity.", inline=False)
        em.add_field(name="Rule 5", value="If you see something against the rules or something that makes you feel unsafe, let staff know. We want this server to be a welcoming space!", inline=False)
        em.add_field(name="Rule 6", value="Any punishment by staff is valid and cannot be appealed unless banned, if you would like to appeal a ban you need proof and good reasoning on why you should be let back in the server.", inline=False)
        em.add_field(name="Rule 7", value="No back talking to staff that will either result in a warn, mute, or kick.", inline=False)
        em.add_field(name="Rule 8", value="Staff is not permitted to abuse power, if a member of the server feels as if they staff is abusing power please talk to one of the administrators of the server and or owner.", inline=False)
        em.add_field(name="Rule 9", value="Failure to follow any of these rules staff is allowed to give any punishment within reason.", inline=False)
        if interaction.guild.id == guildid.guild:
            await interaction.response.send_message(embed=em)
        else:
            await interaction.response.send_message("This command is not available in this server", ephemeral=True)

async def setup(bot):
    await bot.add_cog(server(bot))