from attr import has
import discord
from discord import client
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands.core import has_permissions
import os
from os import getenv
import discord.voice_client
import datetime

load_dotenv()
token = getenv("BotToken")

#embeds
embed_eiche=discord.Embed(title="B a u m", description="B A U M")
embed_eiche.add_field(name="Baum.", value="*Baum *", inline=False)
embed_eiche.set_image(url="https://www.lfl.bayern.de/mam/cms07/iab/bilder/quercus_robur_wuchs_in_flur.jpg")

embed_busch_1=discord.Embed(title="B u s c h", description="B U S C H")
embed_busch_1.add_field(name="Busch.", value="*Busch *", inline=False)
embed_busch_1.set_image(url="https://www.mimikama.at/wp-content/uploads/2020/02/076.jpg")

embed_möp=discord.Embed(title="M ö p", description="M Ö P")
embed_möp.add_field(name="Möp.", value="*Möp *", inline=False)
embed_möp.set_image(url="https://photos.desired.de/5d/19/4a/fb0dc887388901d75358146712_cmUgMCA2NTADNTlmZDg4MDc1NDE=_giphy-6.gif")

#file reading

bot_helper = []
with open(os.path.dirname(os.path.realpath(__file__)) + "\\cogs\\helper\\bot_helper.txt", "r") as f:
    for line in f:
        bot_helper.append(line.replace("\n", ""))

mia = []
with open(os.path.dirname(os.path.realpath(__file__)) + "\\cogs\\helper\\mia.txt", "r") as f:
    for line in f:
        mia.append(line.replace("\n", ""))

#Helper?

def is_bot_helper(ctx):
    for x in bot_helper :
        if str(x) == str(ctx.message.author.id) :
            return True
    return False

#On Server?

def is_on_tempel(ctx):
    if ctx.guild.id == 716018221282492528 :
        return True
    return False

#Random Defs

def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

def is_numeric(probe):
    try:
        probe = int(probe)
        return True
    except:
        return False

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

    for filename in os.listdir("C:\\Users\\mbjki\\Desktop\\DC-Bot\\cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            print(str(filename))
    print("")

#time
time_now = None
def set_time():
    global time_now
    now_local = datetime.now().astimezone()
    time_normal = f"{now_local.isoformat(timespec='seconds')}"
    time_temp = time_normal[11:]
    time_now = time_temp[:-6]

#helper commands

@client.command()
async def ping(ctx):
    if is_bot_helper(ctx) == True:
        print("Ping by: " + str(ctx.message.author) + " With ID: " + str(ctx.message.author.id))
        await ctx.channel.send("pong")
    else:
        print("Ping falsly sent by: " + str(ctx.message.author) + " With ID: " + str(ctx.message.author.id))

@client.command(aliases = ["purge"])
@has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    print(str(ctx.message.author) + " cleared " + str(amount) + " messages in channel: " + str(ctx.channel) + " on Server: " + str(ctx.guild.name))
    await ctx.channel.purge(limit=amount)
    await ctx.send("Done.", delete_after=5.0)

@client.command(aliases = ["h_purge", "h_clear"])
async def helper_clear(ctx, amount=1):
    if is_bot_helper == True:
        print(str(ctx.message.author) + " cleared " + str(amount) + " messages in channel: " + str(ctx.channel) + " on Server: " + str(ctx.guild.name))
        await ctx.channel.purge(limit=amount+1)
        await ctx.send("Done.", delete_after=5.0)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
    print(str(ctx.message.author) + " kicked member: " + str(member) + " on Server: " + str(ctx.guild.name))
    await member.kick()
    await ctx.send("Done.")

@client.command(aliases = ["h_kick"])
async def helper_kick(ctx, member : discord.Member):
    if is_bot_helper == True:
        print(str(ctx.message.author) + " kicked member: " + str(member) + " on Server: " + str(ctx.guild.name))
        await member.kick()
        await ctx.send("Done.")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member):
    print(str(ctx.message.author) + " banned member: " + str(member) + " on Server: " + str(ctx.guild.name))
    await member.ban()
    await ctx.send("Done.")

@client.command(aliases = ["h_ban"])
async def helper_ban(ctx, member : discord.Member):
    if is_bot_helper == True:
        print(str(ctx.message.author) + " banned member: " + str(member) + " on Server: " + str(ctx.guild.name))
        await member.ban()
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
async def hide(ctx):
    if is_bot_helper(ctx) == True:
        await client.change_presence(status=discord.Status.offline)
        print("Stealth +10")
        await ctx.send("Stealth +10.", delete_after=10.0)
    else:
        await ctx.send("No.")

@client.command()
async def show(ctx):
    if is_bot_helper(ctx) == True:
        await client.change_presence(status=discord.Status.online)
        print("Stealth -10")
        await ctx.send("Stealth -10")
    else:
        await ctx.send("No.")

#tempel support
@client.command()
async def support(ctx):
        await ctx.send("Help is on the wayyy!", delete_after=120.0)
        channel = client.get_channel(814622615712694272)
        tempel_tsup = discord.utils.get(ctx.guild.roles, id=732948396352077885)
        tempel_sup = discord.utils.get(ctx.guild.roles, id=721807454106812520)
        tempel_dsup = discord.utils.get(ctx.guild.roles, id=838103735544447027)
        tempel_mod = discord.utils.get(ctx.guild.roles, id=840696091849916427)
        tempel_cv = discord.utils.get(ctx.guild.roles, id=732947023233417287)
        tempel_dev = discord.utils.get(ctx.guild.roles, id=830152957173563402)
        tempel_admin = discord.utils.get(ctx.guild.roles, id=721974730826973205)
        tempel_tl = discord.utils.get(ctx.guild.roles, id=814560022088384572)
        tempel_owner = discord.utils.get(ctx.guild.roles, id=721721071329345548)
        await channel.send(f"Der User " + str(ctx.message.author) + f" braucht hilfe! {tempel_tsup.mention} {tempel_sup.mention} {tempel_dsup.mention} {tempel_tl.mention} ")

#more Random Commands
@client.command()
async def shutdown(ctx):
    if is_bot_helper(ctx) == True:
        print("shutting down...")
        await client.close()
    else:
        await ctx.send("No.")

@client.command()
async def baum(ctx):
    await ctx.send(embed=embed_eiche, delete_after=10.0)

@client.command()
async def busch(ctx):
    await ctx.send(embed=embed_busch_1, delete_after=10.0)

@client.command()
async def möp(ctx):
    await ctx.send(embed=embed_möp, delete_after= 10.0)

@client.command(aliases = ["pr"])
async def presence(ctx):
    if is_bot_helper(ctx) == True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="t$help"))
    else:
        print("Something went wrong.")

@client.command()
@has_permissions(mute_members=True)
async def mute(ctx, member : discord.Member):
    await member.edit(mute=True)
    await ctx.send("Done.")

@client.command(aliases = ["h_mute"])
async def helper_mute(ctx, member : discord.Member):
    if is_bot_helper(ctx) == True:
        await member.edit(mute=True)
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
@has_permissions(mute_members=True)
async def unmute(ctx, member : discord.Member):
    await member.edit(mute=False)
    await ctx.send("Done.")

@client.command(aliases = ["h_unmute"])
async def helper_unmute(ctx, member : discord.Member):
    if is_bot_helper(ctx) == True:
        await member.edit(mute=False)
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
@has_permissions(deafen_members=True)
async def deaf(ctx, member : discord.Member):
    await member.edit(deaf=True)
    await ctx.send("Done.")

@client.command(aliases = ["h_deaf"])
async def helper_deaf(ctx, member : discord.Member):
    if is_bot_helper(ctx) == True:
        await member.edit(deaf=True)
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
@has_permissions(deafen_members=True)
async def undeaf(ctx, member : discord.Member):
    await member.edit(deaf=False)
    await ctx.send("Done.")

@client.command(aliases = ["h_undeaf"])
async def helper_undeaf(ctx, member : discord.Member):
    if is_bot_helper(ctx) == True:
        await member.edit(deaf=False)
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
@has_permissions(move_members=True)
async def disconnect(ctx, member : discord.Member):
    await member.edit(voice_channel=None)
    await ctx.send("Done.")

@client.command(aliases = ["h_disconnect"])
async def helper_disconnect(ctx, member : discord.Member):
    if is_bot_helper(ctx) == True:
        await member.edit(voice_channel=None)
        await ctx.send("Done.")
    else:
        await ctx.send("No.")

@client.command()
async def prepare(ctx):
    if ctx.author.voice.channel.name == "T3stbOt - HUB":
        category = discord.utils.get(ctx.guild.categories, name = "HUB")
        await ctx.guild.create_voice_channel(f"{ctx.message.author}'s channel", category = category, overwrites=None)
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name = f"{ctx.message.author}'s channel")
        await ctx.author.move_to(voice_channel)

@client.event
async def on_voice_state_update(member, before, after):
    voice_channel = discord.utils.get(member.guild.voice_channels, name = f"{member}'s channel")
    if before.channel is voice_channel and after.channel is not voice_channel:
        if voice_channel is None:
            return
        if voice_channel.members == []:
            await voice_channel.delete()

client.run(token)