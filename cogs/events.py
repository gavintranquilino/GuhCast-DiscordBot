import discord
from discord.ext import commands, tasks
from itertools import cycle

bot_status = cycle(['with myself', 'with your mom', 'https://linktr.ee/guhcast'])

# --EVENTS--


class EVENTS(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Background task loop
    @tasks.loop(seconds=20, count=None, reconnect=True)
    async def status_loop(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(next(bot_status)))

    # Bot online and status event
    @commands.Cog.listener()
    async def on_ready(self):
        self.status_loop.start()
        print('GuhBot v3 is online and ready! C:')

    # Member joined Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} joined the server. C:')

    # Member left Event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left the server. :C')


# Cog Setup
def setup(client):
    client.add_cog(EVENTS(client))
