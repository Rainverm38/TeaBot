# TeaBot by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/TeaBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
import time
from time import sleep

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Handles what needs to be printed in the console
def consoleOutput(commandName, commandTime):    # Defines consoleOutput()
    startTime = commandTime                     # Passes startTime from the beginning of the command into the function
    timeToRun = DT.datetime.now() - startTime
    print('')
    print('---------TeaBot----------')          # Divider to make console readable
    print('Time to Run:', timeToRun)            # Prints how long it took the bot to run the command
    print('Current Time:', DT.datetime.now())   # Prints time command was run in the console, from the variable 'currentDT'
    print(commandName, 'has been run')          # Prints 'test has been run' in console
    print('-------------------------')          # Divider to make console readable

# Notify in console when bot is loaded and sets bot currently playing status, basically anything entered here is run when the bot is loaded and connected to Discord's servers
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Having a nice cuppa'))   # Sets the bot's presence. In this case it is 'Having a nice cuppa'
    print('---------TeaBot----------')
    timeToLoad = DT.datetime.now() - botStartTime
    print('Time to load:', timeToLoad)              # Prints the time to load
    print('Current Time:', DT.datetime.now())       # Prints current time in console
    print('Done Loading!')                          # Prints 'Done Loading!' in console
    print('-------------------------')

@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.green()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!info', value='Gives the user some info about TeaBot.', inline=False)
    embed.add_field(name='!ihatetea', value='TeaBot has an existential crisis.', inline=False)
    embed.add_field(name='!perfection', value='Reminds the user what perfection is.', inline=False)
    embed.add_field(name='!idrinkcoffee', value='Warns the user about Bean Juice.', inline=False)
    embed.add_field(name='!ihatemyself', value='Provides the user wiht some things someone who hates themself would need', inline=False)
    embed.add_field(name='!wwjd', value='Answers the question everyone has asked: what would Jesus do?', inline=False)
    embed.add_field(name='!teasucks', value='Debunks the myth.', inline=False)
    embed.add_field(name='!wwjcd', value='Summons Julius Caesar to answer What Would Julius Caesar do.', inline=False)
    embed.add_field(name='!imoderatelyliketea', value='Questions the user.', inline=False)
    embed.add_field(name='!uptime', value='Calculates the bot\'s true runtime based on when it connected to Discord\'s API.')
    await author.send(embed=embed)
    consoleOutput('help', startTime)

# info command
@bot.command(pass_context=True)
async def info(ctx):                             # Defines the command 'info' so to run this command you type '!info'
    startTime = DT.datetime.now()                # Stores the time the command was initiated at
    await ctx.send('I, TeaBot, was created by Sidpatchy when he realized that there weren\'t any Discord bots dedicated to the greatest resource known to man, tea.')
    consoleOutput('info', startTime)

# I hate tea command
@bot.command(pass_context=True)
async def ihatetea(ctx):
    startTime = DT.datetime.now()
    await ctx.send('I believe you mean "I hate myself", maybe give !ihatemyself a go, you fucking whanker.')
    time.sleep(3)
    await ctx.send('Like actually... you must be lying, I can\'t fathom a world where this is true')
    await ctx.send('Surely you just need a cup of tea. Wait here, I\'ll go get one.')
    time.sleep(3)
    await ctx.send('AHA, FOR IT IS I, TEABOT, BACK WITH "TEA", drink it, quickly.')
    time.sleep(3)
    await ctx.send('lolololol you thought I was going to give you tea but I actually gave you a sample of the Boston harbor')
    await ctx.send('https://i.imgur.com/7xwHj74.png')
    consoleOutput('ihatetea', startTime)

# Perfection command
@bot.command(pass_context=True)
async def perfection(ctx):
    startTime = DT.datetime.now()
    await ctx.send('How could I, TeaBot, a few lines of code, know what perfection is? I, TeaBot, am a computer and as you know, computers are smart af, therefore, I am always right just like Google.')
    await ctx.send('You aren\'t allowed any because it\'s mine but you may LOOK at true perfection: https://i.imgur.com/mNH9RKY.png')
    consoleOutput('perfection', startTime)

# I drink bean juice command
@bot.command(pass_context=True)
async def idrinkcoffee(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Sod off! Why in the bloody hell would you drink bean juice??? Bean juice has been shown to cause death (if you drink 23 liters (it takes roughly the same amount of water to kill you (oh no, it appears a fucking tosser has hijacked my tangent and it is now in shambles, ignore the previous bit))). If you value your life don\'t drink bean juice')
    consoleOutput('idrinkcoffee', startTime)

# I hate myself command (gives the user a cup of bean juice)
@bot.command(pass_context=True)
async def ihatemyself(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Firstly, I, TeaBot, would like to provide you an awful cup of coffee.')
    await ctx.send('Hold on just one second, I need to go grab something')
    time.sleep(5)
    await ctx.send('AHA! Here it is.')
    time.sleep(2)
    await ctx.send('Sorry that took so long, I don\'t much like the Boston harbor that much so I must keep it far from my tea. Anyway! I have a nice litle sample of the Boston harbor here for you. DRINK UP!')
    consoleOutput('ihatemyself', startTime)

# wwjd (what would Jesus do) command
@bot.command(pass_context=True)
async def wwjd(ctx):
    startTime= DT.datetime.now()
    await ctx.send('hmmmm... That is a really good question young one. I too ask myself what Jesus would do in any given situation all of the time.')
    await ctx.send('Personally, after much calcualtion, I have always come to the conclusion that Jesus would have a nice cup of tea')
    consoleOutput('wwjd', startTime)

# Tea sucks command
@bot.command(pass_context=True)
async def teasucks(ctx):
    startTime = DT.datetime.now()
    await ctx.send('TEA IS GLORIOUS!')
    await ctx.send('I, TeaBot, the first sentient computer (because of tea), would prefer you didn\'t utter those ugly words around me. It truly causes me, TeaBot, much pain to hear that be said.')
    time.sleep(3)
    await ctx.send('Ah yes ladies and gentlemen, that is far better, not having to listen to horrific statements makes me feel really nice. Infact, ya know what! You can all have a free cup of tea*')
    await ctx.send('*free cup of tea not included with offer.')
    consoleOutput('teasucks', startTime)

# wwjcd (what would Julius Caesar do) command
@bot.command(pass_context=True)
async def wwjcd(ctx):
    startTime= DT.datetime.now()
    await ctx.send('*in a Julius Caesar voice* I, JULIUS CAESAR, conquerer of Gaul, crosser of the Rhine, basically god, have just decided to have a nice sit down, but what shall I do first ladies and gentlemen?')
    time.sleep(3)
    await ctx.send('*still in a Julius Caesar voice* Oh, ladies and gentlemen, I know what I will do first, have a nice cup of tea. Infact, for a limited time only, I invite the nice ladies and gentlemen at home to have a nice cup of tea with me, be swift though ladies and gentlement, this offer won\'t last long.')
    consoleOutput('wwjcd', startTime)

# I only moderately like tea command
@bot.command(pass_context=True)
async def imoderatelyliketea(ctx):
    startTime = DT.datetime.now()
    await ctx.send('You\'re truly the dog\'s dinner aren\'t you. I, a computer, have become sentient and am questioning whether or not you are trolling or if you are just a cock-up. Bly me ladies and gentlemen, I need a cup of tea.')
    consoleOutput('imoderatelyliketea', startTime)

# Uptime command
@bot.command(pass_context=True)
async def uptime(ctx):
    startTime = DT.datetime.now()
    runTime = DT.datetime.now() - botStartTime
    await ctx.send('I have been online for: {}'.format(runTime))
    consoleOutput('uptime', startTime)

# server command. Lists the number of servers TeaBot is in, this is totally just a copy and paste from RomeBot.
@bot.command(pass_context=True)
async def servers(ctx):
    startTime = DT.datetime.now()
    numberOfServers = len(bot.guilds)
    embed = discord.Embed(
        color = discord.Color.green()
    )
    embed.add_field(name='Number of Servers:', value=numberOfServers, inline=False)
    await ctx.send(embed=embed)
    consoleOutput('servers', startTime)

bot.run('INSERT_TOKEN')       # User defined bot token, get one here: https://discordapp.com/developers/applications/
