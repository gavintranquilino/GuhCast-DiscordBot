import discord
import random
from discord.ext import commands

# --INTERACTION--


class INTERACTION(commands.Cog):

    def __init__(self, client):
        self.client = client

    # shoot command
    @commands.command()
    async def shoot(self, ctx, *, member):
        await ctx.message.delete()
        shoot_responses = [
            ' **gets shot**',
            ' get shot lmao',
            ' omg sis shoot for the sky :woman_fairy::sparkles::white_heart::kissing_heart: now aim it at your skull :sparkles::sparkles::woman_fairy: :purse: :hibiscus:',
            ' **gets shot and fucking dies**',
            ' bleeds to death'
        ]
        if member == 'myself':
            await ctx.send(ctx.author.mention + random.choice(shoot_responses))
        elif member == 'me':
            await ctx.send(ctx.author.mention + random.choice(shoot_responses))
        elif member == 'yourself':
            await ctx.send('So you think you can kill me off that easily huh?')
        elif member == '<@!707593703530692665>':
            await ctx.send('Really? Trying to kill me? smh')
        else:
            await ctx.send(member + random.choice(shoot_responses))

# Cog Setup


def setup(client):
    client.add_cog(INTERACTION(client))
