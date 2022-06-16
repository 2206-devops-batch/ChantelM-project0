# import sys
# sys.path.append("..")
from dotenv import dotenv_values
from discord.ext import commands
import discord
# from Games.tictactoeGame import TicTacToe
# from GameData import ttt_games as tttGames
import tictactoeServer


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

    @tictactoe.command(description="Provide mention (@username) of user to challenge")
    async def challenge(self, ctx, username:discord.Member): #requires mentioning member
        #TODO: go through server
        # test = self.bot.get_user(username.id) #FIXME: self.bot error
        completed = tictactoeServer.initiate_game_data(username.name, ctx.author.name, username, ctx.author)

        if completed[0]:
            await completed[1][0].send(f"{ctx.message.author.name} challenged you to a game of tic-tac-toe. Accept to make the first move!")
            await completed[1][1].send(f" has been sent a request for tic-tac-toe")
        else:
            await ctx.send(completed[1])

    @tictactoe.command(description="To start game, provide a row followed by a column (between 0 and 2): '0 0'")
    async def accept(self, ctx, row, column, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.initiate_game_start(ctx.author.name, str(row), str(column), gameID)
        
        if completed[0]:
            await ctx.send(f"Game updated with your move and opponent notified")
            await completed[3].send(completed[2])
        else:
            await ctx.send(f"Error: {completed[1]}")
    
    @tictactoe.command(description="Deny request")
    async def deny(self, ctx, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.deny_game_start(ctx.author.name)
        print("deny", completed)

        if completed[0]:
            completed[3].send(completed[2])
            ctx.send(f"{completed[3].name} has been notified you do not wish to play tictactoe.")
        else:
            await ctx.send(f"Error: {completed[2]}")

    @tictactoe.command(description="Provide a row followed by a column (between 0 and 2): 0 0")
    async def move(self, ctx, row, column, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.player_move(ctx.author.name, str(row), str(column), gameID)
        
        if completed[0]:
            if completed[1]:
                await completed[3].send(completed[2])
                await ctx.send(completed[2])
            else:
                await ctx.send(f"Game updated with your move and opponent notified")
                await completed[3].send(completed[2])
        else:
            await ctx.send(f"Error: {completed[1]}")

    @tictactoe.command(description="Exit tictactoe game")
    async def quit(self, ctx, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.end_game(ctx.author.name, False, gameID)
        print("quit", completed)

        sendStr = completed[2] if completed[0] else f"Error: {completed[1]}"
        
        await ctx.send(sendStr)
        await completed[3].send(sendStr)


#TODO: load as an extension vs just adding cog
# def setup(bot: commands.Bot):
#     bot.add_cog(TicTacToeCog(bot))

if __name__ == "__main__":
    bot1 = commands.Bot(command_prefix=dotenv_values("../.env")["COMMAND_PREFIX"])
    bot1.add_cog(TicTacToeCog(bot1))
    bot1.run(dotenv_values("../.env")['DISCORD_TEST_TOKEN'])
 