import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.messages = True  # Ensure the bot can read messages
bot = commands.Bot(command_prefix="!leobot ", intents=intents)

@bot.command(name="via")
async def via(ctx):
    await ctx.send("ME AND VIA ARE OVER! STOP TALKING ABOUT HER!")

@bot.command(name="credits")
async def credits(ctx):
    await ctx.send("credits to coder of the bot, owner id: 1184539864360816772")

@bot.command(name="jakov")
async def jakov(ctx):
    await ctx.send("jakov my baby boy:heart::heart: (volim te jakov)")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message contains the desired phrases
    if "i love you" in message.content.lower():
        if message.author.name.lower() == "vioxla":
            await message.channel.send("NO!:broken_heart: WE'RE OVER")
        else:
            await message.channel.send(f"Thank you {message.author.mention} :heart: love you too baby:heart:")
    elif "mat" in message.content.lower():
        await message.channel.send("uhh about mat, I kidnapped him and put him in my backpack, just to make sure via is mine:heart:")
    elif "keep leone" in message.content.lower():
        await message.channel.send("SERIOUSLY?! WE'RE OVER VIA!")

    # Allow commands to process after this event handler
    await bot.process_commands(message)

@bot.command(name="i love you")
async def loveyoutoo(ctx):
    await ctx.send("thank you :heart: love you too")

@bot.command(name="mat")
async def mat(ctx):
    await ctx.send("actually sorry mat I can pay you some money and I take her all for myself:fire::heart:")

# Fetch the token from the environment variable
token = os.getenv("DISCORD_TOKEN")

# Run the bot with the token from the environment variable
bot.run(token)
