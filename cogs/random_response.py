from discord.ext import commands
import random

#Responses
responses_035 = ["Ist n faules Stück",
                "Is(s)t ne geile Gurke",
                "Ist säxy",
                "Ist belastet",
                "Ist n komischer Typ",
                "Hat ne *Belastungsstörung*",
                "Ist unser Gurkenkönig",
                "stinkt",
                "Is tired...",
                "Ist ne perverse Maske >:)"
                ]

responses_999 = ["Mag keine Gurken >:(",
                "Frisst unsere Süßigkeiten weg >:(",
                "Ist ne coole Sau",
                "Ist unser Kaiser",
                "Ist ein ~~Abzock~~ guter Psychiater",
                "stinkt"
                ]

responses_magges = ["Hat nen säxy Schnurrbart",
                    "Der Schnurrbart ihres Vertrauens!",
                    "Klatscht alle(s)",
                    "stinkt"
                    ]

responses_naomi = [ "stinkt",
                    "ist am kaken",
                    "Hat ne fette Kakawurst auf ihrem Kopf :P"
                    ]

responses_nuke = ["Nukeeeeeee"]

responses_mia = ["bonkt alle(s)",
                "*bonk * AUA!"
                ]

responses_pillow = ["Pillowwwwww"]

responses_uwu = [" = rape me"]

responses_bubble = ["mag Katzenbilder",
                    "stinkt",
                    "Is(s)t keine Katze"
                    ]

responses_mystery = ["Muss sein Aim finden",
                    "stinkt"
                    ]

responses_liltim = ["Tim Lil",
                    "stinkt",
                    "Leader of Community"
                    ]

responses_koogi = ["Kooooooogi"]

responses_richard = ["Richard"]

responses_henri = ["ist ne heiße Trap",
                    "stinkt",
                    "ist keine Belastung"
                    ]

responses_dennis = ["Vernascht alle(s).",
                    "Ist der Obersimp",
                    "Hat schöne Haare~",
                    "ist sexyyy",
                    "ist der echte Unge!"
                    ]

#Maincode
class random_response(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == "hello bot":
            print(f"{str(message.author)} said *hello bot*. Here is his/her ID: {str(message.author.id)}")
            await message.channel.send("Hey!")
            await message.author.send("Hey, du hast mich Kontaktiert! Um eine Liste meiner Befehle zu bekommen, schick  t$help [1/2]  in einen Serverchat!", delete_after=30.0)
        elif message.content.lower() == "035":
            await message.channel.send(f"{random.choice(responses_035)}")
        elif message.content.lower() == "999":
            await message.channel.send(f"{random.choice(responses_999)}")
        elif message.content.lower() == "magges":
            await message.channel.send(f"{random.choice(responses_magges)}")
        elif message.content.lower() == "naomi":
            await message.channel.send(f"{random.choice(responses_naomi)}")
        elif message.content.lower() == "nuke":
            await message.channel.send(f"{random.choice(responses_nuke)}")
        elif message.content.lower() == "mia":
            await message.channel.send(f"{random.choice(responses_mia)}")
        elif message.content.lower() == "pillow":
            await message.channel.send(f"{random.choice(responses_pillow)}")
        elif message.content.lower() == "uwu":
            await message.channel.send(f"{random.choice(responses_uwu)}")
        elif message.content.lower() == "bubble":
            await message.channel.send(f"{random.choice(responses_bubble)}")
        elif message.content.lower() == "mystery":
            await message.channel.send(f"{random.choice(responses_mystery)}")
        elif message.content.lower() == "lil tim":
            await message.channel.send(f"{random.choice(responses_liltim)}")
        elif message.content.lower() == "henri":
            await message.channel.send(f"{random.choice(responses_henri)}")
        elif message.content.lower() == "ricardo":
            await message.channel.send(f"{random.choice(responses_richard)}")
        elif message.content.lower() == "dennis":
            await message.channel.send(f"{random.choice(responses_dennis)}")

def setup(client):
    client.add_cog(random_response(client))