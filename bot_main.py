
from discord.ext import commands, tasks
from sensible_vars import get_sensible_vars
import discord
import os


bot = commands.Bot(command_prefix=">")

bot.CHECK_STATUS_FILE = True
bot.VAR_ACTIVITY_BOT = "var_activity_bot"
bot.VARS_STRING = "vars_status"
bot.ERRORS_STRING = "error_history"
bot.STATUS_CODE_DISCT = None
bot.MINUTES_TO_WAIT_LOOP = 10
bot.ERRORS = []
bot.FILE_PATH = os.path.join(os.getcwd(),"status_code.json")
bot.ERROR_URL_IMG = "https://cdn3.iconfinder.com/data/icons/basicolor-signs-warnings/24/182_warning_notice_error-512.png"

bot.DEFAUL_CHANNEL_ID, token = get_sensible_vars()

@bot.event
async def on_ready():
    print("Bot is ready")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def load(ctx, extention="BasicCommands"):
    await ctx.send(f'Cargando {extention}')
    bot.load_extension(f'cogs.{extention}')

@bot.command()
async def unload(ctx, extention="BasicCommands"):
    await ctx.send(f'Retirando {extention}')
    bot.unload_extension(f'cogs.{extention}')

@bot.command()
async def reload(ctx,extention="BasicCommands"):
    await ctx.send(f'Recargando {extention}')
    bot.unload_extension(f'cogs.{extention}')
    bot.load_extension(f'cogs.{extention}')


bot.run(token)

