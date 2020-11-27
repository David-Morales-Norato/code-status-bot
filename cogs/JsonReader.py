from cogs.utils.load_status_code import read_status_file
from discord.ext import commands, tasks
import discord
import time
import os


class JsonReader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.load_file_status.start()
    
    def check_flag(self):
        return self.bot.CHECK_STATUS_FILE

    def change_flag(self):
        self.bot.CHECK_STATUS_FILE = not self.bot.CHECK_STATUS_FILE


    # Loop to load the JSON file and get all the needed information
    @commands.check(check_flag)
    @tasks.loop(seconds = 5)
    async def load_file_status(self):
        
        # Reaading JSON file
        self.bot.STATUS_CODE_DISCT = read_status_file(self.bot.FILE_PATH,self.bot.VAR_ACTIVITY_BOT)

        # Setting the main_var as the bot activity
        main_var = self.bot.STATUS_CODE_DISCT.get(self.bot.VAR_ACTIVITY_BOT)
        name_activity = main_var + ": " + str(self.bot.STATUS_CODE_DISCT.get(self.bot.VARS_STRING).get(main_var,None))
        activity = discord.Game(name = name_activity)
        await self.bot.change_presence(activity=activity)


        # Getting errors to track them
        errors_collection = list(zip(*self.bot.STATUS_CODE_DISCT[self.bot.ERRORS_STRING]))

        if(errors_collection != []):

            # If there are new errors, it sends them through an embed to the server
            ids_tmp, errors_tmp = list(errors_collection[0]), list(errors_collection[1])
            errors = [errors_tmp[len(self.bot.ERRORS)+i] for i in range(max(len(ids_tmp) - len(self.bot.ERRORS),0))]
            if (errors != []):
                embed = discord.Embed(title = "Errores nuevos en el código:", color = discord.Colour.red())
                embed.set_thumbnail(url = self.bot.ERROR_URL_IMG)
                for error in errors:
                    embed.add_field(name="Error", value=error, inline=False)
                await self.bot.get_channel(self.bot.DEFAUL_CHANNEL_ID).send(embed = embed)

            self.bot.ERRORS = errors_tmp
        


    # Command to stop the loop which reads the JSON file
    @commands.command()
    async def stop_load_file_loop(self, ctx):
        self.change_flag()
        await ctx.send("Parando loop")

    # Command to start the loop which reads the JSON file
    @commands.command()
    async def start_load_file_loop(self, ctx):
        self.change_flag()
        await ctx.send("Comenzando loop")
    

def setup(bot):
    bot.add_cog(JsonReader(bot))