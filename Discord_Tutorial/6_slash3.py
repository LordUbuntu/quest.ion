from SECRET import TOKEN
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord import Intents, Interaction, SlashOption, ChannelType, Member


intents = Intents.all()
bot = commands.Bot(intents=intents)

@bot.slash_command(
    name="nickname",
    description="Example 4",
    guild_ids=[524420519609499648]
)
async def ex4(interaction: Interaction,
    member: Member = SlashOption(
        name="member",
        description="Choose a member",
        required=True
    ),
    channel: GuildChannel = SlashOption(
        channel_types=[ChannelType.text]
    ),
):
    await channel.send(f"Member's server nickname: {member.display_name}")

    await interaction.send("Sent!", ephemeral=True)


bot.run(TOKEN)
