import discord
from discord.ext import commands
import random

embed_miabonk=discord.Embed(title="B o n k", description="B O N K")
embed_miabonk.add_field(name="Get bonked", value="*Bonk *", inline=False)
embed_miabonk.set_image(url="https://i.kym-cdn.com/photos/images/masonry/002/051/072/a4c.gif")

dick_lengh_string = ""

def random_dick_lengh():
    global dick_lengh_string
    dick_lengh_array = []
    x = random.randrange(1, 10)
    while x >= 0:
        dick_lengh_array.append("=")
        x -= 1
    dick_lengh_string = "".join(dick_lengh_array)

class mia_commands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def bonk(ctx):
        await ctx.send(embed=embed_miabonk)

    @commands.command(aliases=["pp"])
    async def dicklengh(self, ctx):
        global dick_lengh_string
        random_dick_lengh()
        await ctx.send(f"Dicklengh: 8{dick_lengh_string}D")

    #@commands.command(aliases=["sc"])
    #async def simpcheck(ctx, member : discord.Member , rolls = 1):
    #    x = 0
    #    while not x == int(rolls):
    #        simpdetector = random.randrange(1, 420)
    #        if simpdetector == 7 or simpdetector == 42 or simpdetector == 69 or simpdetector == 420:
    #            await ctx.send(f"{member.mention} (b)ist KEIN SIMP! #{simpdetector}")
    #        else: 
    #            await ctx.send(f"{member.mention} SIMP!")
    #        x += 1
    #    x = 0

def setup(client):
    client.add_cog(mia_commands(client))