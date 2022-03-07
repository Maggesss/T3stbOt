import discord
from discord.ext import commands
import datetime

embed_help_normal=discord.Embed(title="Help - normal", description="Bot Prefix: t$")
embed_help_normal.add_field(name="8ball", value="| t$8ball /Frage\ | Befrage die magische Miesmuschel über dein Schicksal mit Ja/Nein Fragen!", inline=False)
embed_help_normal.add_field(name="hide", value="| t$hide | Versteckt den Bot *Ninjamodus aktiviert! * |", inline=False)
embed_help_normal.add_field(name="show", value="Deaktiviert den Ninjamodus wieder :) |", inline=False)
embed_help_normal.add_field(name="baum", value="| t$baum | Zeigt dir einen Baum.", inline=False)
embed_help_normal.add_field(name="busch", value="| t$busch | Zeigt dir einen Busch.", inline=False)
embed_help_normal.add_field(name="help", value="| t$help /normal|music|admin|mia\ | Die weiteren Help-Seiten.", inline=False)
embed_help_normal.set_footer(text="Gruß, Magges, der Schnurrbart ihres Vertrauens")

embed_help_music=discord.Embed(title="Help - music", description="Bot Prefix: t$")
embed_help_music.add_field(name="leave", value="| t$leave | Verlässt deinen Voicechat.", inline=False)
embed_help_music.add_field(name="join", value="| t$join | Joint deinem Voicechat.", inline=False)
embed_help_music.add_field(name="play", value="| t$play [90s/deutschrap/eurobeat/film/jazz/rock/snadmann/schlager/xmas] | Spielt in deinem VoiceChannel Jazz!", inline=False)
embed_help_music.add_field(name="help", value="| t$help /normal|music|admin|mia\ | Die weiteren Help-Seiten.", inline=False)
embed_help_music.set_footer(text="Gruß, Magges, der Schnurrbart ihres Vertrauens")

embed_help_admin=discord.Embed(title="Help - admin", description="Bot Prefix: t$")
embed_help_admin.add_field(name="clear", value="| t$clear /Anzahl\ | Löscht /Anzahl\ an Nachrichten im ausgeführten Chat - Aliases: purge |", inline=False)
embed_help_admin.add_field(name="kick", value="| t$kick /@Member\ | Selbsterklärend :) |", inline=False)
embed_help_admin.add_field(name="ban", value="| t$ban /@Member\ | Selbsterklärend :) |", inline=False)
embed_help_admin.add_field(name="mute", value="| t$mute /@Member\ | Selbsterklärend :) |", inline=False)
embed_help_admin.add_field(name="unmute", value="| t$unmute /@Member\ | Selbsterklärend :) |", inline=False)
embed_help_admin.add_field(name="disconnect", value="| t$disconnect /@Member\ | Selbsterklärend :) |", inline=False)
embed_help_admin.set_footer(text="Gruß, Magges, dein Schnurrbart des Vertrauens")

embed_miahelp_1=discord.Embed(title="Secret MiaHelp! - 1", description="Bot Prefix: t$")
embed_miahelp_1.add_field(name="bonk", value="| t$bonk | *Bonk * ", inline=False)
embed_miahelp_1.add_field(name="dick", value="| t$dick | Aliases: pp", inline=False)
embed_miahelp_1.set_footer(text="Gruß, Magges, dein Schnurrbart des Vertrauens")

#time
time_now = None
def set_time():
    global time_now
    now_local = datetime.now().astimezone()
    time_normal = f"{now_local.isoformat(timespec='seconds')}"
    time_temp = time_normal[11:]
    time_now = time_temp[:-6]

class help_commands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx, arg="normal"):
        set_time
        if arg == "normal":
            await ctx.send(embed=embed_help_normal, delete_after=60.0)
        elif arg == "music":
            await ctx.send(embed=embed_help_music, delete_after=60.0)
        elif arg == "admin":
            await ctx.send(embed=embed_help_admin, delete_after=60.0)
        elif arg == "mia":
            await ctx.send(embed=embed_miahelp_1, delete_after=60.0)
        print(f"{time_now} | {str(ctx.message.author)} requested Help \"{arg}\" on   <| {str(ctx.guild)} |>")

def setup(client):
    client.add_cog(help_commands(client))