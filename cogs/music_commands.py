from discord.ext import commands
from discord import client
import discord.voice_client
from discord import FFmpegPCMAudio
import random
import os
import datetime

def is_connected(ctx):
    voice_client = discord.utils.get(ctx.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

def getWav(genre):
    gWlist = []
    for file in os.listdir("C:\\Users\\mbjki\\Desktop\\DC-Bot\\cogs\\musik\\" + str(genre.lower())):
        gWlist.append("C:\\Users\\mbjki\\Desktop\\DC-Bot\\cogs\\musik\\" + str(genre.lower()) + "\\" + file)
    return (discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source= f"{random.choice(gWlist)}"))

#time
time_now = None
def set_time():
    global time_now
    now_local = datetime.now().astimezone()
    time_normal = f"{now_local.isoformat(timespec='seconds')}"
    time_temp = time_normal[11:]
    time_now = time_temp[:-6]

#Maincode
class music_commands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Tritt zuerst einem Sprachkanal bei!")
        elif ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
        else:
            voice_channel = ctx.author.voice.channel
            await ctx.voice_client.move_to(voice_channel)
        print(f"[ {str(ctx.message.author)} ] summoned some music in channel: [ {str(voice_channel)} ] on Server: [ {str(ctx.guild)} ]")

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, arg):
        if ctx.author.voice is None:
            await ctx.send("Tritt zuerst einem Sprachkanal bei!")
        elif ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
        else:
            voice_channel = ctx.author.voice.channel
            await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
        try:
            vc = ctx.voice_client
            vc.play(getWav(arg))
        except:
            await ctx.send("Something went wrong!")
            print("Can't resolve.")
    
    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused.")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resumed.")

def setup(client):
    client.add_cog(music_commands(client))

#work in progress