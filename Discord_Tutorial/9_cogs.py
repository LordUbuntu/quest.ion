from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Interaction, SlashOption 
import os
# prefix
bot = commands.Bot(command_prefix="$")


if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")


@bot.slash_command(
    name="reload",
    description="Reload a cog",
    guild_ids=[524420519609499648]
)
async def reload(interaction: Interaction,
    extension: str = SlashOption(
        name="extension",
        description="Cog name",
        required=True,
    ),
):
    bot.reload_extension(f"cogs.{extension}")
    await interaction.send(f"{extension} has been loaded ✅")

bot.run(TOKEN)