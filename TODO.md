## Modules Used:

[python-dotenv](https://pypi.org/project/python-dotenv/)
[Discord Developer Portal](https://discord.com/developers/docs/intro)
[discord.py](https://discordpy.readthedocs.io/en/stable/)

- [Discord API](https://discordpy.readthedocs.io/en/stable/api.html)
  [dpytest](https://dpytest.readthedocs.io/en/latest/)

## TODO:

- [ ] README
- [ ] Attempt ansible

## Completed:

- [x] discord bot initial deploy
  - [x] read message
  - [x] assign tic-tac-toe command
- [x] tic-tac-toe
  - [x] create class
    - [x] start game
    - [x] stop game
    - [x] game play
      - [x] enter a move
      - [x] update board
      - [x] check for a winner
      - [x] **str** for ttt class
- [x] commands
  - [x] ?tictactoe [ ] functional
    - [x] ?challenge [x] functional
      - [x] player1: ?tictactoe challenge username
        - [x] verify 2 users are not already associated with a current gameID
        - [x] store gameID: { players: [username, initiator], game: TicTacToe()}
      - [x] send private message from bot inviting player
    - [x] ?accept [ ] functional
      - [x] second player ?tictactoe accept row column
        - [x] find the appropriate gameID with username in players & game=None
        - [x] update associated gameID['game']:
          - [x] t3.start_game()
          - [x] t3.make_move(row, column) via gameID['game'].move(row, column)
    - [x] ?deny (for denying request) [ ] functional
      - [x] second player ?tictactoe deny
      - [x] find game with author as player
        - [x] if more than one gameID['game] is None with author in players:
          - [x] list appropriate gameIDs (with challenger) and display how to specify
        - [x] else grab players[0] and send a notification of denial
    - [x] ?move row column gameID [ ] functional
      - [x] if gameID specified use that game
      - [x] else find gameID and display appropriate command
      - [x] parse row and column into integers
        - [x] check in bounds & selected place is none
          - [x] if issue display error
      - [x] update board via t3.make_move(row, column)
      - [x] notify opponent of game update
    - [x] ?quit [ ] functional
      - [x] find gameID
      - [x] del gameID['game]
      - [x] notify both game has been ended by author
- [x] discord bot deploy with game
  - [x] initial commands
  - [x] commands functionality without server functions
  - [ ] commands functionality with server functions
  - [x] general game Loop implemented
- [x] discord bot deploy with game
  - [x] initial commands
  - [x] commands functionality without server functions
  - [x] commands functionality with server functions
  - [x] general game Loop implemented
- [x] commands
  - [x] ?tictactoe [x] functional [x] server function
    - [x] store to separate server app via tictactoeServer.py functions
    - [ ] stretch goal: database
    - [x] ?challenge [x] functional [x] server function
    - [x] ?accept [x] functional [x] server function
    - [x] ?deny (for denying request) [x] functional [ ] server function
    - [x] ?move row column gameID [x] functional [ ] server function
    - [x] ?quit [x] functional [x] server function
- [x] Store Persistent Data TODO: determine best method using a server to store data
  - [x] call to local server
  - [x] store games as objects on server
- [ ] Testing:
  - [ ] [unittest](https://docs.python.org/3/library/unittest.html)
    - [x] tic tac toe game
    - [x] tic tac toe server
- [x] Automate:
  - [x] automate testing
    - [x] src/server/tictactoe
  - [x] if passed, start
