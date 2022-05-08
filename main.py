from SECRET import TOKEN
from nextcord.ext import commands
from nextcord import Intents, Interaction, ButtonStyle, ui


class Confirm(ui.View):
    def __init__(self, Qa, Qb, Qc, Qd, Qi):
        super().__init__(timeout=120)
        self.value = None
        self.Qa = Qa
        self.Qb = Qb
        self.Qc = Qc
        self.Qd = Qd
        self.Qi = Qi

    @ui.button(label="A", style=ButtonStyle.green, row=1)
    async def A(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Answer A", ephemeral=True)
        self.value = True
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)

    @ui.button(label="B", style=ButtonStyle.red, row=2)
    async def B(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Answer B", ephemeral=True)
        self.value = False
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)

    @ui.button(label="C", style=ButtonStyle.grey, row=2)
    async def C(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Answer C", ephemeral=True)
        self.value = False
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)

    @ui.button(label="D", style=ButtonStyle.blurple, row=2)
    async def D(self, button: ui.Button, interaction: Interaction):
        await interaction.send("Answer D", ephemeral=True)
        self.value = False
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)


intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def question(ctx, text, Qa, Qb, Qc, Qd, ans_index):
    """Asks the user a question"""
    view = Confirm(Qa, Qb, Qc, Qd, ans_index)
    await ctx.send(text, view=view)

    await view.wait()
    if view.value is None:
        print("Timed out...")
    elif view.value:
        print("Confirmed...")
    else:
        print("Cancelled...")


bot.run(TOKEN)
