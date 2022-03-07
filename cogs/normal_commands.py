import discord
from discord.ext import commands
import random

responses_8ball = [
                "Eines Tages vielleicht!", 
                "Gar nichts.", 
                "Keins von beiden.", 
                "Ich glaube ehr nicht.",
                "Nein.",
                "Nein :(",
                "Nein :C",
                "Nein! >:C",
                "Ja.",
                "Ja. :)",
                "Ja :D",
                "Ja >:D",
                "Frag doch einfach nochmal!"
                ]

class normal_commands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases = ["8ball"])
    async def _8ball(ctx, *, question):
        await ctx.send(f"Frage: {question}\nAntwort: {random.choice(responses_8ball)}")

def setup(client):
    client.add_cog(normal_commands(client))