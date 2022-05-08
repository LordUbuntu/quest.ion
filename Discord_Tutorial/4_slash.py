from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Interaction

intents = Intents.all()
bot = commands.Bot(intents=intents)


@bot.slash_command(
    name="ping",
    description="pong!",
    guild_ids=[524420519609499648]
)
async def ex2(interaction: Interaction):
    await interaction.send("pong!")


bot.run(TOKEN)
