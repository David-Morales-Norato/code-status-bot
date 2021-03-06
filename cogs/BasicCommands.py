from cogs.utils.load_status_code import read_status_file
from discord.ext import commands, tasks
from itertools import cycle
import discord
import time
import os


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Clear the last {amount} msgs in the chat. by default amount is 100
    @commands.command()
    async def clear(self,ctx,amount = 100 ):
        await ctx.channel.purge(limit = amount)
        

    # This command shows the status of your program by sending the vars in the JSON file through an embed to the server
    @commands.command()
    async def show_status(self,ctx):
        embed = discord.Embed(title = "Estatus del código:", color = discord.Colour.green())
        dict_vars = self.bot.STATUS_CODE_DISCT[self.bot.VARS_STRING]
        for key, value in dict_vars.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.send(embed = embed)

    # This command shows all the errors of your program by sending the erros in the JSON file through an embed to the server
    @commands.command()
    async def show_errors(self,ctx):
        embed = discord.Embed(title = "Errores del código:", color = discord.Colour.red())
        embed.set_thumbnail(url = self.bot.ERROR_URL_IMG )
        errors = self.bot.STATUS_CODE_DISCT[self.bot.ERRORS_STRING]
        for error in errors:
            embed.add_field(name="Error", value=error, inline=False)
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(BasicCommands(bot))