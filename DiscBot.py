from dotenv import dotenv_values
from discord.ext import commands
from BotCogs.tictactoeCog import TicTacToeCog

COGS_TO_ADD = [TicTacToeCog]


class DiscordBot:
    def __init__(self, selected_prefix):
        self.cBot = commands.Bot(command_prefix=selected_prefix)

        @self.cBot.event
        async def on_ready():
            print("game_bot logged in")

    def login_bot(self, secret_key):
        self.cBot.run(secret_key)

    def add_all_cogs(self): 
        #TODO: try implement using a text file of Module Class cycle through 'from {Module} import {class}(self.cBot)'
    
        for i in COGS_TO_ADD:
            self.cBot.add_cog(i(self.cBot))
    

if __name__ == "__main__":
    t1 = DiscordBot(dotenv_values(".env")["COMMAND_PREFIX"])
    t1.add_all_cogs()
    t1.login_bot(dotenv_values(".env")['DISCORD_TEST_TOKEN'])
