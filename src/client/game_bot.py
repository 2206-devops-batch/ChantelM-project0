from dotenv import dotenv_values
from discord.ext import commands


bot = commands.Bot(command_prefix=dotenv_values(".env")['COMMAND_PREFIX'])
bot.lanHost = dotenv_values(".env")['HOST']
bot.lanPort = int(dotenv_values(".env")['PORT'])

@bot.event


async def on_ready():
    print("game_bot logged in")

bot.load_extension("cogs.tictactoe")

bot.run(dotenv_values(".env")['DISCORD_TEST_TOKEN'])
