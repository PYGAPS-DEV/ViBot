import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True  # Ensure the bot can read messages
bot = commands.Bot(command_prefix="!leobot ", intents=intents)

@bot.command(name="via")
async def via(ctx):
    await ctx.send("VIA IS MINE!!:heart:")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message contains the desired phrases
    if "i love you leone" in message.content.lower() or "i love you" in message.content.lower():
        await message.channel.send(f"Thank you {message.author.mention} :heart: love you too baby:heart:")

    # Allow commands to process after this event handler
    await bot.process_commands(message)

@bot.command(name="i love you")
async def loveyoutoo(ctx):
    await ctx.send("thank you :heart: love you too")
    
@bot.command(name="mat")
async def mat(ctx):
    await ctx.send("yo sorry mat but we gotta share her or yk i can pay you some money and i take her all for myself:fire::heart:")

bot.run("MTMxMzk2MDU0MzcwMjQ4NzA3MA.G5_tiK.cy2-M04mg1ic9k1Qb_mcbWyNYXDsZPbmbTVw5Y")
