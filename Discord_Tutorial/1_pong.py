import os
from nextcord.ext import commands
from SECRET import TOKEN


# prefix
bot = commands.Bot(command_prefix="$")


@bot.command()
async def ping(ctx: commands.Context):
    # print("pong")

    await ctx.send("pong")

@bot.command()
async def hello(ctx: commands.Context):
    # print("pong")

    await ctx.send("bye")

bot.run(TOKEN)
