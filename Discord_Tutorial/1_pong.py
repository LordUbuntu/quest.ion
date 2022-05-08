import os
from nextcord.ext import commands

secret_code = os.environ['discord_secret']
# prefix
bot = commands.Bot(command_prefix="$")


@bot.command()
async def ping(ctx: commands.Context):
    # print("pong")

    await ctx.send("pong")


bot.run(secret_code)
