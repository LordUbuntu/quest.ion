from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Interaction, ButtonStyle, ui, SelectOption
# modified https://github.com/nextcord/nextcord/blob/master/examples/views/dropdown.py


class FavouriteColour(ui.View):
    def __init__(self):
        super().__init__(timeout=120)

    options = [
            SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')
    ]

    @ui.select(placeholder="Choose your favourite colour", min_values=1, max_values=1, options=options)
    async def colour(self, select : ui.Select, interaction: Interaction):
        await interaction.send(f'{select.values[0]}', ephemeral=True)

    @ui.button(label='Confirm', style=ButtonStyle.gray)
    async def cancel(self, button: ui.Button, interaction: Interaction):
        await interaction.send('Confirmed', ephemeral=True)
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)




#######################################################################################################

intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def select(ctx):
    await ctx.send('Choose your favourite colour...', view=FavouriteColour())


bot.run(TOKEN)
