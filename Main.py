from ImageReader import getHealthInfo
from PIL import ImageGrab
import discord
from discord.ext import commands, tasks

#Checks screen every 2 seconds to see if characters health is below half
#If below half health, open a bright visual demanding the user to get health, as well as play a loud noise
#This will repeat until the player is dead or gets health above 40%

connections = {}
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
     print("logged in")

@bot.command()
async def Start(ctx):
    colorCheck.start(ctx)

@tasks.loop(seconds=2)
async def colorCheck(ctx):
    client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    # If bot is already in call, just play the sound
    if client:
        vc = connections[ctx.guild.id]
        connections.update({ctx.guild.id: vc})
        if getHealthInfo(ImageGrab.grab()):
            vc.play(discord.FFmpegPCMAudio('Audio/GetHealth.wav'))
    # If bot is not in call, joins the users channel, plays the sound
    else:
        vc = await ctx.author.voice.channel.connect()
        connections.update({ctx.guild.id: vc})
        if getHealthInfo(ImageGrab.grab()):
            vc.play(discord.FFmpegPCMAudio('Audio/GetHealth.wav'))

@bot.command()
async def Stop(ctx):
    if ctx.guild.id in connections:  # Check if the guild is in the cache.
        vc = connections[ctx.guild.id]
        vc.disconnect()
        del connections[ctx.guild.id]  # Remove the guild from the cache.
        del ctx # And delete.
    else:
        await ctx.send("type shit")

bot.run("")