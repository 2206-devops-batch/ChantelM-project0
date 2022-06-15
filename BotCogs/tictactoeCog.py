# from attr import s
# import sys
# sys.path.append("..")
from dotenv import dotenv_values
from discord.ext import commands

# sys.path.append("..")
# from Games.tictactoeGame import TicTacToe
# ttt = TicTacToe('x', 'o')
# ttt.display_board()
"""
Discord library's commands framework is used to extend bot's functionality.
"""

class TicTacToeCog(commands.Cog):
    """
    Commands, listeners, and state are organized using Discord library's defined Cogs class within the commands framework.
    Each cog is a subclass of commands.cog.
    https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html?highlight=cogs#
    """
    def __init___(self, bot):
        self.bot = bot

    @commands.command(description="Provide name of user to challenge")
    async def tictactoe(self, ctx, username):
        # ?help tic_tac_toe from commands framework
        await ctx.send(f"Challenge {username} to tic tac toe by creating private channel and sending invite")

    # @commands.command(description="Provide name of user to challenge")
    # async def tic_tac_toe(self, ctx, username):
    #     # ?help tic_tac_toe from commands framework
    #     await ctx.send(f"Challenge {username} to tic tac toe")



if __name__ == "__main__":
    bot = commands.Bot(command_prefix=dotenv_values("../.env")["COMMAND_PREFIX"])
    bot.add_cog(TicTacToeCog(bot))
    bot.run(dotenv_values("../.env")['DISCORD_TEST_TOKEN'])
 