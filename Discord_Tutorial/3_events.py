from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Message

intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.event
async def on_message(message: Message):
    if "thank" in message.content:
        await message.add_reaction("🙂")



bot.run("OTcxODk2Njk1OTMzNzg4MjMx.GWvn7l.e9sDdAFTzRZVdMlcKLcKycOvqO9Z7l3ZY2LDpU")
