from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Interaction, ButtonStyle, ui

# modified https://github.com/nextcord/nextcord/blob/master/examples/views/confirm.py


class Confirm(ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.value = None

    @ui.button(label="Confirm", style=ButtonStyle.green, row=1)
    async def confirm(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Confirming", ephemeral=True)
        self.value = True
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)

    @ui.button(label="Cancel", style=ButtonStyle.red, row=2)
    async def cancel(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Cancelling", ephemeral=True)
        self.value = False
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)


#######################################################################################################


intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def btn(ctx):
    """Asks the user a question to confirm something."""
    view = Confirm()
    await ctx.send("Do you want to continue?", view=view)

    await view.wait()
    if view.value is None:
        print("Timed out...")
    elif view.value:
        print("Confirmed...")
    else:
        print("Cancelled...")


bot.run("OTcxODk2Njk1OTMzNzg4MjMx.GWvn7l.e9sDdAFTzRZVdMlcKLcKycOvqO9Z7l3ZY2LDpU")
