from dotenv import dotenv_values
from discord.ext import commands
import discord
import socket
import sys
import sys
sys.path.append("../../../")

"""
Commands extension provides the basis for integrating commands and subcommands.
"""

#FIXME: dotenv variables with cogs?
HOST='localhost'
PORT=9031


class Tictactoe(commands.Cog):
    """
    TicTacToe subclass of discord.ext.commands.Cog class used for organizing commands, listeners, and state.

    TODO: look into cogs as inter-command communication
    """
    def __init__(self, bot):
        self.bot = bot
        self.srvr_HOST = HOST
        self.srvr_PORT = PORT

    def contact_server(self, msg):
        lanClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lanClient.connect((self.srvr_HOST, self.srvr_PORT))

        lanClient.send(msg.encode('utf-8'))
        return lanClient.recv(1024).decode("utf-8")
    
    @commands.group(description="Parent command for tic tac toe game")
    async def tictactoe(self, ctx):
        pass

    @tictactoe.command(description="Provide mention (@username) of user to challenge")
    async def challenge(self, ctx, username:discord.Member): #requires mentioning member
  
        results = self.contact_server(f"1 {username.name} {ctx.author.name} {username.id} {ctx.author.id}").split()
        
        if results[0] == "True":
            user0 = await self.bot.fetch_user(int(results[1]))
            user1 = await self.bot.fetch_user(int(results[2]))

            await user0.send(f"{ctx.message.author.name} challenged you to a game of tic-tac-toe."
                "Decide on your first move and accept by using the command '?tictactoe accept <row> <column>'!")
            await user1.send(f" {user0.name} has been sent a request for tic-tac-toe")

        else:
            results.pop(0)
            results = " ".join(results)
            await ctx.send(results)

    @tictactoe.command(description="To start game, provide a row followed by a column (between 0 and 2): '0 0'")
    async def accept(self, ctx, row, column, gameID=None):

        res = self.contact_server(f"2 {ctx.author.name} {row} {column} {gameID}").split()

        if res[0] == 'True':
            opp = int(res.pop(2))
            res.pop(0)
            res.pop(1)
            
            opponent = await self.bot.fetch_user(opp)
            msg = " ".join(res)

            await ctx.send(f"Game updated with your move {opponent.name} and notified")
            await opponent.send(msg)
        else:
            res.pop(0)
            msg = "Error: " + " ".join(res)
            await ctx.send(msg)
    
    @tictactoe.command(description="Deny request")
    async def deny(self, ctx, gameID=None):

        res = self.contact_server(f"3 {ctx.author.name} None ").split()
        print(res)
        
        if res[0] == 'True':
            msg = " ".join(res[3:])
            opponent = await self.bot.fetch_user(int(res[2]))
            opponent.send(msg)
            ctx.send(f"{opponent.name} has been notified you do not wish to play tictactoe.")

        else:
            res.pop(0)
            msg = "Error: " + " ".join(res)
            await ctx.send(msg)

    @tictactoe.command(description="Provide a row followed by a column (between 0 and 2): 0 0")
    async def move(self, ctx, row, column, gameID=None):

        res = self.contact_server(f"4 {ctx.author.name} {row} {column} {gameID}").split()
        
        if res[0] == 'True':
            opponent = await self.bot.fetch_user(int(res[2]))
            msg = " ".join(res[3:])

            await opponent.send(msg)
            await ctx.send(msg)

        else:
            res.pop(0)
            msg = "Error: " + " ".join(res)
            await ctx.send(msg)

    @tictactoe.command(description="Exit tictactoe game")
    async def quit(self, ctx, gameID=None):
 
        res = self.contact_server(f"5 {ctx.author.name} False {gameID} False").split()

        if res[0] == 'True':
            opponent = await self.bot.fetch_user(int(res[2]))
            msg = " ".join(res[3:])

            await opponent.send(msg)
            await ctx.send(msg)
        else:
            res.pop(0)
            msg = "Error: " + " ".join(res)
            await ctx.send(msg)

    @tictactoe.command(description="Exit tictactoe game")
    async def autoplay(self, ctx):
        res = self.contact_server(f"6 None")
        await ctx.send(res)


def setup(bot):
    bot.add_cog(Tictactoe(bot))
