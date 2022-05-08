from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents

intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def ex1(ctx: commands.Context, id: int):
    guild = ctx.guild
    channel = guild.get_channel(959519611034931270) #test-2
    member = guild.get_member(id)

    await channel.send(f"Member's server nickname: {member.display_name}")


bot.run('OTcxODk2Njk1OTMzNzg4MjMx.GWvn7l.e9sDdAFTzRZVdMlcKLcKycOvqO9Z7l3ZY2LDpU')


# get member nickname then send it to a specific channel
