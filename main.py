import os
import discord
from discord.ext import commands
from server import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TARGET_ROLE_NAME = "Member"
CHANNEL_ID = 1394248637269409833

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

@bot.event
async def on_member_update(before, after):
    new_roles = [r for r in after.roles if r not in before.roles]
    for role in new_roles:
        if role.name == TARGET_ROLE_NAME:
            channel = after.guild.get_channel(CHANNEL_ID)
            if channel:
                embed = discord.Embed(
                    description=f"### Welcome to Vibe Chemistry {after.mention}✌️\n\n" 
                               "💌 Your in-game invitation has been sent!\n\n"
                               "🎨 Pick your own colour: <#1393469201225613382>\n\n"
                               "📌 Overview: <#1412651833574559774>\n\n"
                               "🔰 If you're new to GW2, check out: <#1300774903003480175>\n\n"
                               "⛩️ Everything about the guild potions and synthesizers: [Guild Hall](https://discord.com/channels/1170458558484201543/1394218637778354249)\n\n"
                               "🛡️ Useful builds for every game mode: [GW2 Builds](https://discord.com/channels/1170458558484201543/1360871848258048175)\n\n"
                               "📅 GW2 dailies are posted here: <#1204824236175138917>\n\n"
                               "🎮 Need help or want to play together? <#1349786696027476052>\n\n"
                               "Glad to have you here – enjoy your stay! 😊🧃\n",
                    color=0x8B5CF6
                )
                embed.set_thumbnail(url=after.avatar.url if after.avatar else after.default_avatar.url)
                await channel.send(embed=embed)

if __name__ == "__main__":
    keep_alive()


    bot.run(os.getenv("DISCORD_TOKEN"))




