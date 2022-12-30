# cog that handles the music in voice channels
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
owners = [375797651486015488, ]
guilds = [1015609486225965102, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners), guild_ids = set(guilds))

class music(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
    
def setup(bot):
    bot.add_cog(music(bot))