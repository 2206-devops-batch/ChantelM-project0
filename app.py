from dotenv import dotenv_values
from DiscBot import DiscordBot

# initialize discord bot with command prefix
t1 = DiscordBot(dotenv_values(".env")["COMMAND_PREFIX"])


# login discord bot
t1.login_bot(dotenv_values(".env")['DISCORD_TEST_TOKEN'])