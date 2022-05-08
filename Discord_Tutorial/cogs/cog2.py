from nextcord.ext import commands
from nextcord import Client

class Cog2(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command()
    async def c2(self, ctx: commands.Context):
        await ctx.send("Hello from cog 2!")


def setup(bot):
    bot.add_cog(Cog2(bot))