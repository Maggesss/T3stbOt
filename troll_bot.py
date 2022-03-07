import discord
from discord import client
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import datetime
import random

load_dotenv()
token = getenv("BotToken")

#get ready
client = commands.Bot(command_prefix = "t$")
client.remove_command('help')

@client.event
async def on_ready():
    print("Login accomplished")

    #Server-counter
    guild_count = 0

    #Guckt welche Server
    for guild in client.guilds:
        #Sagt welche Server
        print(f"- {guild.id} (name: {guild.name})")

        #Server-counter aktualisierung
        guild_count = guild_count + 1

    print(f"Bot is in {str(guild_count)} guilds. \n")
    print("")

#time
time_now = None
def set_time():
    global time_now
    now_local = datetime.now().astimezone()
    time_normal = f"{now_local.isoformat(timespec='seconds')}"
    time_temp = time_normal[11:]
    time_now = time_temp[:-6]

@client.command(aliases=["sm"])
async def spam_mention(ctx, user : discord.Member, count=10):
    helper_var = 0
    while not helper_var == count:
        await ctx.send(str(f"{user.mention}"))
        helper_var = helper_var + 1

dick_lengh_string = ""

def random_dick_lengh():
    global dick_lengh_string
    dick_lengh_array = []
    x = random.randrange(1, 10)
    while x >= 0:
        dick_lengh_array.append("=")
        x -= 1
    dick_lengh_string = "".join(dick_lengh_array)

@client.command(aliases=["pp"])
async def dicklengh(ctx):
    global dick_lengh_string
    random_dick_lengh()
    await ctx.send(f"Dicklengh: 8{dick_lengh_string}D")

simpdetector = 0
x = 0

def random_number_1_to_420():
    global simpdetector
    simpdetector = random.randrange(1, 420)

@client.command(aliases=["sc"])
async def simpcheck(ctx, member : discord.Member , rolls = 1):
    global simpdetector, x
    while not x == rolls:
        random_number_1_to_420
        if simpdetector == 7 or simpdetector == 42 or simpdetector == 69 or simpdetector == 420:
            await ctx.send(f"{member.mention} (b)ist KEIN SIMP! #{simpdetector}")
        else: 
            await ctx.send(f"{member.mention} SIMP!")
        x += 1
    x = 0

@client.command()
async def shutdown(ctx):
    if ctx.message.author.id == 444460699025014784:
      print("shutdown")
      try:
        await client.close()
      except:
        print("EnvironmentError")
        client.clear()
    else:
      await ctx.send("You do not own this bot!")

client.run(token)