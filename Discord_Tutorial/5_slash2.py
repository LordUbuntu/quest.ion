from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Interaction, SlashOption


intents = Intents.all()
bot = commands.Bot(intents=intents)

@bot.slash_command(
    name="number",
    description="Example 3",
    guild_ids=[524420519609499648]
)
async def ex3(interaction: Interaction,
    num: int = SlashOption(
        name="num",
        description="Choose a number",
        required=True,
        choices=[1, 2, 3, 4, 5],
    ),
):
    await interaction.send(f"{num} was selected", ephemeral=True)


bot.run(TOKEN)
