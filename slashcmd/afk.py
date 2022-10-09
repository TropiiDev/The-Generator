# pip install imports
import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get

# local imports
import guildid
from afks import afks

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("AFK Online")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick=remove(message.author.display_name))
            except:
                pass
            await message.channel.send(f"{message.author.mention} is no longer AFK")
        
        for id, reason in afks.items():
            member = get(message.guild.members, id=id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                await message.reply(f"{member.name} is AFK: {reason}")

    @app_commands.command(name="afk", description="Set your status to AFK")
    @app_commands.guilds(guildid.guilds)
    async def afk(self, interaction: discord.Interaction, *, reason:str = None):
        if interaction.user.id in afks.keys():
            afks.pop(interaction.user.id)
        else: 
            try:
                await interaction.user.edit(nick=f"[AFK] {interaction.user.display_name}")
            except:
                pass

        afks[interaction.user.id] = reason
        em = discord.Embed(title=f":zzz: Member AFK", description=f"{interaction.user.mention} has went AFK", color=0x00ff00)
        em.set_thumbnail(url=interaction.user.avatar)
        em.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        em.add_field(name="AFK Note: ", value=reason)
        await interaction.response.send_message(embed=em)

async def setup(bot):
    await bot.add_cog(afk(bot))