import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.messages = True  # Ensure the bot can read messages
bot = commands.Bot(command_prefix="!leobot ", intents=intents)

@bot.command(name="via")
async def via(ctx):
    await ctx.send("VIA IS MINE!!:heart:")

@bot.command(name="jakov")
async def jakov(ctx):
    await ctx.send("jakov the joker lice :smiling_imp: (gutbitnika ***i dont know what that is***)")
    
@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message contains the desired phrases
    if "i love you leone" in message.content.lower() or "i love you" in message.content.lower():
        await message.channel.send(f"Thank you {message.author.mention} :heart: love you too baby:heart:")
    elif "mat" in message.content.lower():
        await message.channel.send("uhh about mat, i kidnapped him and put him in my backpack, just to make sure via is mine:heart:")

    # Allow commands to process after this event handler
    await bot.process_commands(message)

@bot.command(name="i love you")
async def loveyoutoo(ctx):
    await ctx.send("thank you :heart: love you too")
    
@bot.command(name="mat")
async def mat(ctx):
    await ctx.send("actually sorry mat i can pay you some money and i take her all for myself:fire::heart:")

# Fetch the token from the environment variable
token = os.getenv("DISCORD_TOKEN")

# Run the bot with the token from the environment variable
bot.run(token)
