import discord
from discord import app_commands
from discord.ext import commands

# local imports
import guildid

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("About Online")

    @app_commands.command(name="about", description="About the bot - hidden from members")
    @app_commands.guilds(guildid.guilds)
    async def about(self, interaction: discord.Interaction):
        em = discord.Embed(title="About", description=None, color = interaction.user.color)
        em.add_field(name="Creator: ", value="Tropiiツ#0001")
        em.add_field(name="Purpose: ", value="To help you manage your server")
        em.add_field(name="Support Server: ", value="[Support Server Link](https://discord.gg/mu4XBRNkBj)")
        em.add_field(name="Invite: ", value="[Invite The Generator](https://discord.com/api/oauth2/authorize?client_id=987757575812558848&permissions=552373161014&scope=bot%20applications.commands)")
        em.add_field(name="Source Code: ", value="[Github Code](https://github.com/WepWop/The-Generator/)")
        em.add_field(name="Website: ", value="[The Generator Website](https://thegenerator.dev/)") 
        em.add_field(name="Prefix: ", value="`/`")

        await interaction.response.send_message(embed=em, ephemeral=True)

async def setup(bot):
    await bot.add_cog(about(bot))