import discord
from tokens import TOKEN 



bot = discord.Client()
help_message = """
"""

asudha_message = {
    "uwu": True,
    ':flushed:': True,
    'sex': True
} 

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Hello World"))
    print("startd")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("s!help"):
        await message.channel.send(help_message)
    for word in message.content.split():
        if word.lower() in asudha_message:
            await message.delete()



bot.run(TOKEN)