#cog for reaction commands
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client(intents=intents)
owners = [375797651486015488, ]
guilds = [1015609486225965102, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners), guild_ids = set(guilds))


class reactions(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    react = SlashCommandGroup("react", "react with funny images")

    @react.command(name="darncat", description="do i give a darn cat") 
    async def darncat(self, ctx):
        await ctx.respond("https://media.discordapp.net/attachments/897944272756674564/1054568722121105449/darnCat_1.gif") 

    @react.command(name="copecat", description="cope harder cat") 
    async def copecat(self, ctx): 
        await ctx.respond("https://tenor.com/view/cope-cry-about-it-seethe-cope-harder-cope-cope-gif-22973511") 

    @react.command(name="spicescat", description="cat got the spices") 
    async def spicescat(self, ctx): 
        await ctx.respond("https://media.discordapp.net/attachments/753030834440896693/1054956285474386020/elgato.gif") 
        
    @react.command(name="stfubunny", description="bunny telling you to quit yappin ni-") 
    async def spicescat(self, ctx): 
        await ctx.respond("https://tenor.com/view/buddy-keep-yapping-keep-yapping-your-mouth-buddy-keep-yapping-your-mouth-n-rabbit-gif-25286735") 
        
    @react.command(name="fucat", description="cat flipping the bird") 
    async def fucat(self, ctx): 
        await ctx.respond("https://tenor.com/view/mean-cat-cat-fu-gif-23644413") 

    @react.command(name="huhcat", description= "you are gonna have to run that by him again") 
    async def huhcat(self, ctx): 
        await ctx.respond("https://media.discordapp.net/attachments/897944272756674564/1055865233241030717/suscat.gif") 

def setup(bot):
    bot.add_cog(reactions(bot))