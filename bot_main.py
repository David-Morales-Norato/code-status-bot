
from discord.ext import commands, tasks
from cogs.utils.load_status_code import read_setup_file

import discord
import os


bot = commands.Bot(command_prefix=">")


setup_dict = read_setup_file("setup.json")



# Sensible vars 
bot.FILE_PATH = setup_dict["json_file_path"] 
bot.DEFAUL_CHANNEL_ID = setup_dict["default_channel_id"] 
token = setup_dict["token"]

# Optional vars
bot.VAR_ACTIVITY_BOT =setup_dict["var_activity_bot"] 
bot.VARS_STRING = setup_dict["vars_string"] 
bot.ERRORS_STRING = setup_dict["errors_string"] 
bot.ERROR_URL_IMG =  setup_dict["error_url_img"] 
bot.STATUS_CODE_DISCT = None
bot.MINUTES_TO_WAIT_LOOP = 10
bot.ERRORS = []



# This event shows up when the bot is ready to run.
# When the bot is ready, it import all funcitonalities in cogs folder
@bot.event
async def on_ready():
    
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f'cogs.{filename[:-3]}')
    print("Bot is ready")


# Command to load an extention manually
@bot.command()
async def load(ctx, extention="BasicCommands"):
    await ctx.send(f'Cargando {extention}')
    bot.load_extension(f'cogs.{extention}')


# Command to load an extention manually
@bot.command()
async def unload(ctx, extention="BasicCommands"):
    await ctx.send(f'Retirando {extention}')
    bot.unload_extension(f'cogs.{extention}')

# Command to load an extention manually
@bot.command()
async def reload(ctx,extention="BasicCommands"):
    await ctx.send(f'Recargando {extention}')
    bot.unload_extension(f'cogs.{extention}')
    bot.load_extension(f'cogs.{extention}')

bot.run(token)

