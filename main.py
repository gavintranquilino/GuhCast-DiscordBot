import discord
import os
from discord.ext import commands

botToken = input('What is the bot token?\n')

# command prefix
client = commands.Bot(command_prefix='guh ')

# function to se if its GuhBean


def is_it_guhbean(ctx):
    return ctx.author.id == 450414958421868554

# cog loader command, loads extension


@client.command()
@commands.check(is_it_guhbean)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded successfully.')

# cog unloader command


@client.command()
@commands.check(is_it_guhbean)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded successfully.')

# cog reloader command, reloads extension


@client.command(aliases=['refresh', 'Refresh', 'Reload'])
@commands.check(is_it_guhbean)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded successfully.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(botToken)
