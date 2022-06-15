# import sys
# sys.path.append("..")
from dotenv import dotenv_values
from discord.ext import commands
# from Games.tictactoeGame import TicTacToe
# from GameData import ttt_games as tttGames
import BotCogs.tictactoeServer as tictactoeServer


"""
Discord library's commands framework is used to extend bot's functionality.
commands: https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
groups for subcommands: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#group
"""

class TicTacToeCog(commands.Cog):
    """
    Commands, listeners, and state are organized using Discord library's defined Cogs class within the commands framework.
    Each cog is a subclass of commands.cog.
    https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html?highlight=cogs#
    """
    def __init___(self, bot):
        self.bot = bot

    @commands.group(description="Parent command for tic tac toe game")
    async def tictactoe(self, ctx):
        pass

    @tictactoe.command(description="Provide name of user to challenge to a game of tic tac toe")
    async def challenge(self, ctx, username):
        #TODO: send private message to username
        created = tictactoeServer.initiate_game_data(username, ctx.message.author.name)

        if created[0]:
            await ctx.send(f"Challenge {username} to tic tac toe by sending a private message")
        else:
            await ctx.send(f"Use gameID {created[1]} to continue game between {ctx.message.author.name} and {username}")

    @tictactoe.command(description="To start game, provide a row followed by a column (between 0 and 2): '0 0'")
    async def accept(self, ctx, row, column, gameID=None):
        #TODO: start game, update board, & send private message to username displaying the board
        await ctx.send(f"Player 0 accepted with first move: {row}, {column}. Send challenger private message with updated board")
    
    @tictactoe.command(description="Deny request")
    async def deny(self, ctx, gameID=None):
        #TODO: send private message to initial challenger
        await ctx.send(f'Let original challenger know {ctx.message.author.name} has denied request')

    @tictactoe.command(description="Provide a row followed by a column (between 0 and 2): 0 0")
    async def move(self, ctx, row, column, gameID=None):
        #TODO: player moves, send updated board to other player in private message if no winner
        await ctx.send(f"Game updated with player's move and opponent notified")

    @tictactoe.command(description="Exit tictactoe game")
    async def quit(self, ctx, gameID=None):
        #TODO: terminate the game and notify all parties
        await ctx.send(f"{ctx.message.author.name} has quit the game of tictactoe.")



if __name__ == "__main__":
    # print(tttGames)
    bot = commands.Bot(command_prefix=dotenv_values("../.env")["COMMAND_PREFIX"])
    bot.add_cog(TicTacToeCog(bot))
    # bot.initiate_game_data()
    # bot.initiate_game_data()
    bot.run(dotenv_values("../.env")['DISCORD_TEST_TOKEN'])
 