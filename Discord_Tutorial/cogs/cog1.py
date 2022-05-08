from nextcord.ext import commands
from nextcord import Client

class Cog1(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command()
    async def c1(self, ctx: commands.Context):
        await ctx.send("Hi from cog 1!")


def setup(bot):
    bot.add_cog(Cog1(bot))