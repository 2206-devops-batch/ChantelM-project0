from dotenv import dotenv_values
from DiscBot import DiscordBot

# initialize discord bot with command prefix
gameBot = DiscordBot(dotenv_values(".env")["COMMAND_PREFIX"])

# add all cogs, currently only tictactoeCog
gameBot.add_all_cogs()

# login discord bot
gameBot.login_bot(dotenv_values(".env")['DISCORD_TEST_TOKEN'])