from discord.ext import commands
import discord
import cogs.tictactoeServer as tictactoeServer

class Tictactoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(description="Parent command for tic tac toe game")
    async def tictactoe(self, ctx):
        pass


    @tictactoe.command(description="Provide mention (@username) of user to challenge")
    async def challenge(self, ctx, username:discord.Member): #requires mentioning member
        #TODO: go through server
  
        completed = tictactoeServer.initiate_game_data(username.name, ctx.author.name, username.id, ctx.author.id)

        if completed[0]:
            completed[1][0] = await self.bot.fetch_user(completed[1][0])
            completed[1][1] = await self.bot.fetch_user(completed[1][1])

            await completed[1][0].send(f"{ctx.message.author.name} challenged you to a game of tic-tac-toe. Accept to make the first move!")
            await completed[1][1].send(f" {completed[1][0].name} has been sent a request for tic-tac-toe")
        else:
            await ctx.send(completed[1])

    @tictactoe.command(description="To start game, provide a row followed by a column (between 0 and 2): '0 0'")
    async def accept(self, ctx, row, column, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.initiate_game_start(ctx.author.name, str(row), str(column), gameID)
        
        if completed[0]:
            opponent = await self.bot.fetch_user(completed[3])

            await ctx.send(f"Game updated with your move and opponent notified")
            await opponent.send(completed[2])
        else:
            await ctx.send(f"Error: {completed[1]}")
    
    @tictactoe.command(description="Deny request")
    async def deny(self, ctx, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.deny_game_start(ctx.author.name)
        print("deny", completed)

        if completed[0]:
            opponent = await self.bot.fetch_user(completed[3])

            opponent.send(completed[2])
            ctx.send(f"{completed[3].name} has been notified you do not wish to play tictactoe.")
        else:
            await ctx.send(f"Error: {completed[2]}")

    @tictactoe.command(description="Provide a row followed by a column (between 0 and 2): 0 0")
    async def move(self, ctx, row, column, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.player_move(ctx.author.name, str(row), str(column), gameID)
        
        if completed[0]:
            opponent = await self.bot.fetch_user(completed[3])

            if completed[1]:
                await opponent.send(completed[2])
                await ctx.send(completed[2])
            else:
                await ctx.send(f"Game updated with your move and opponent notified")
                await opponent.send(completed[2])
        else:
            await ctx.send(f"Error: {completed[1]}")

    @tictactoe.command(description="Exit tictactoe game")
    async def quit(self, ctx, gameID=None):
        #TODO: go through server
        completed = tictactoeServer.end_game(ctx.author.name, False, gameID)
        opponent = await self.bot.fetch_user(completed[3])

        sendStr = completed[2] if completed[0] else f"Error: {completed[1]}"
        
        await ctx.send(sendStr)
        await opponent.send(sendStr)


def setup(bot):
    bot.add_cog(Tictactoe(bot))