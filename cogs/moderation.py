#cog for moderation commands
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import has_role, MissingRole

intents = discord.Intents.default()
intents.members = True
owners = [375797651486015488, ]
guilds = [1015609486225965102, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners), guild_ids = set(guilds))

class moderation(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
    
    moderation = SlashCommandGroup("mod", "moderation commands")
    
    @moderation.command(name = "help", description = "list of moderation commands")
    @commands.has_role('神')
    async def help(self, ctx):
        await ctx.respond("test", ephemeral = True)
    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error, MissingRole):
            await ctx.respond("You do not have permission", ephemeral = True)

def setup(bot):
    bot.add_cog(moderation(bot))