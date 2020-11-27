from cogs.utils.load_status_code import read_status_file
from discord.ext import commands, tasks
from itertools import cycle
import discord
import os

os.listdir(".")

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.load_file_status.start()
    
    def check_flag(self):
        return self.bot.CHECK_STATUS_FILE

    @commands.check(check_flag)
    @tasks.loop(seconds = 5)
    async def load_file_status(self):
        
        self.bot.STATUS_CODE_DISCT = read_status_file(self.bot.FILE_PATH,self.bot.VAR_ACTIVITY_BOT)
        main_var = self.bot.STATUS_CODE_DISCT.get(self.bot.VAR_ACTIVITY_BOT)
        name_activity = main_var + ": " + str(self.bot.STATUS_CODE_DISCT.get(self.bot.VARS_STRING).get(main_var,None))
        activity = discord.Game(name = name_activity)

        await self.bot.change_presence(activity=activity)

    @commands.command()
    async def clear(self,ctx,amount = 100):
        await ctx.channel.purge(limit = amount)
        

    @commands.command()
    async def show_status(self,ctx, var=None):
        embed = discord.Embed(title = "Estatus del código:", color = discord.Colour.green())
        print(self.bot.STATUS_CODE_DISCT)
        print(self.bot.STATUS_CODE_DISCT[self.bot.VARS_STRING])
        dict_vars = self.bot.STATUS_CODE_DISCT[self.bot.VARS_STRING]
        for key, value in dict_vars.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def stop_load_file_loop(self, ctx):
        print("Sdadasd")
        await ctx.send("Parando loop")
        self.load_file_status.stop()

    @commands.command()
    async def start_load_file_loop(self, ctx):
        print("123124")
        await ctx.send("Comenzando loop")
        self.load_file_status.restart()
    

def setup(bot):
    bot.add_cog(BasicCommands(bot))