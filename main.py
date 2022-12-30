import discord
from discord.ext import commands
import os, random
import dotenv 
dotenv.load_dotenv() 
token = str(os.getenv('TOKEN')) 

intents = discord.Intents.default() 
intents.message_content = True 
owners = [375797651486015488, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners))

def eascii():
    print('\n\n')
    print('        _       __          __               ')
    print('  ___  (_)___  / /_  ____  / /_  ____  __  __')
    print(' / _ \/ / __ \/ __ \/ __ \/ __/ / __ \/ / / /')
    print('/  __/ / / / / /_/ / /_/ / /__ / /_/ / /_/ / ')
    print('\___/_/_/ /_/_.___/\____/\__(_) .___/\__, /  ')
    print('                             /_/    /____/   ')

@bot.event 
async def on_ready():
    eascii() 
    print(f'\n{bot.user} is now awake! Woof Woof!') 
    botactivity = discord.Activity(type=discord.ActivityType.playing, name="with /react commands")
    await bot.change_presence(activity=botactivity, status=discord.Status.online)

#check to see if up with latency and date(soon^tm)
@bot.command(name="poke", description="test to see if ein is awake") 
async def poke(ctx): 
    await ctx.respond(f"Grrr {ctx.author.mention}! Latency is {round(bot.latency, 2)}ms.") 

@bot.event 
async def on_message(message): 
    if message.author == bot.user: 
        return 
    if message.content.startswith('cope'): 
        await message.channel.send('https://tenor.com/view/cope-cry-about-it-seethe-cope-harder-cope-cope-gif-22973511') 

images = ['https://cdn.discordapp.com/attachments/1016689681758433330/1056577197852332092/einpfp2.jpeg', 'https://cdn.discordapp.com/attachments/1016689681758433330/1056577197575516191/einpfp1.jpeg']

@bot.command(name="imagebomb")
async def imagebomb(ctx):
    await ctx.send('ok here you go!', file=discord.File(random.choice(('images/einpfp1.jpeg', 'images/einpfp2.jpeg'))))


@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title="Commands",
        description="",
        color=discord.Colour.blurple(),

    )
    embed.add_field(name="General", value="</poke:1056569502852194375> - to test if bot is up\n</help:1056782669104554048> - brings up this menu\n</imagebomb:1056574263081050182> - sends a random image of Ein :dog:", inline=False)
    
    embed.add_field(name="Reactions - react with goofy images/gifs!", value="</react copecat:1056956185804279888>\n</react spicescat:1056956185804279888>\n</react stfubunny:1056956185804279888>\n</react fucat:1056956185804279888>\n</react huhcat:1056956185804279888>\n</react copecat:1056956185804279888>\n</react darncat:1056956185804279888>", inline=False)
 
    await ctx.respond(f"Hello {ctx.author.mention}! \n\nEin is a simple discord bot with a variety of commands including reactions, moderation, and more. Just a past time project of mine and another excuse to learn python. Below is a list of commands that Ein has to offer.\n\nCreated by Walke#2306", embed=embed)

@bot.command(name='rules')
@commands.is_owner()
async def rules(ctx):
    embed = discord.Embed(
        title="rules",
        description="",
        color=discord.Colour.blurple(),

    )
    # embed.add_field()
    # embed.add_field()

    await ctx.respond(f"@everyone")


cogs_list = [
    'reactions',
    'moderation'
    
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run(token)

