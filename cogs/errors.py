import discord
from discord.ext import commands

# --ERRORS--


class ERRORS(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Command Errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # Missing Permissions
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('I don\'t think you have the perms to do that. ಠ_ಠ')

        # Commands Not Found
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('I don\'t think that command exists. Oopsies :expressionless:')

        # Missing Argument
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('I think that you missed a required argument. Mistakes happen ¯\_(ツ)_/¯')

        # Bad Argument
        if isinstance(error, commands.BadArgument):
            await ctx.send('I don\'t think I quite undertand that. Sorry :sweat_smile:')

        # Command Invoke Error
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Invoke Error. In layman\'s terms, something went wrong. :slight_frown:')

        # Missing Any Role
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send('I\'m sorry but you don\'t have the required role/roles to run this command. :grimacing:')

        # Extension Already Loaded
        if isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send(f'The extension you tried to load is already loaded.')

        # Extension Not Found
        if isinstance(error, commands.ExtensionNotFound):
            await ctx.send('Sorry but I couldn\'t find that extension.')

        # Check failure
        if isinstance(error, commands.CheckFailure):
            await ctx.send('I don\'t think you have the facilities for that big man. You **failed** your vibe **check**')

# Cog Setup


def setup(client):
    client.add_cog(ERRORS(client))
