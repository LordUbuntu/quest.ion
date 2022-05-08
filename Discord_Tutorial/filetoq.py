from nextcord import Intents, Interaction, ButtonStyle, ui
from SECRET import TOKEN
from nextcord.ext import commands

with open('questions.txt') as f:
    lines = f.read().splitlines()
Qs = []
qpos = -1

for i in lines:
    if(i[-1] == '?'):
        Qs.append([])
        qpos += 1
    Qs[qpos].append(i)


class Question(ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.value = None
        self.answer = -1

    async def load(self, arg):
        for i in range(len(Qs[arg])-1):
            print("hello")
        
   
    """@ui.button(label='Answer', style=ButtonStyle.red, row=1)
    async def confirm(self, button: ui.Button, interaction: Interaction):
        await interaction.send('Confirming', ephemeral=True)
        self.value = True
        for child in self.children:
            child.disabled = True
        await interaction.edit(view=self)"""
