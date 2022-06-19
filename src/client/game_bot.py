from dotenv import dotenv_values
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event

async def on_ready():
    print("game_bot logged in")

bot.load_extension("cogs.tictactoe")

bot.run(dotenv_values("../../.env")['DISCORD_TEST_TOKEN'])

