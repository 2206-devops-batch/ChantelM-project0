# ChantelM-project0

Project 0: Server Game

## Modules Used:

[python-dotenv](https://pypi.org/project/python-dotenv/)
[Discord Developer Portal](https://discord.com/developers/docs/intro)
[discord.py](https://discordpy.readthedocs.io/en/stable/)

- [Discord API](https://discordpy.readthedocs.io/en/stable/api.html)
  [dpytest](https://dpytest.readthedocs.io/en/latest/)

## TODO:

- [ ] discord bot deploy with game
  - [ ] initial commands
  - [ ] commands functionality without server functions
  - [ ] commands functionality with server functions
  - [ ] game Loop
    - [ ] wait for command
    - [ ] if gameID['game'].active
      - [ ] if correct player, allow move
      - [ ] else notify it is not there turn
    - [ ] if not gameID['game'].active
      - [ ] notify both of board
      - [ ] if not gameID['game'].winner, notify both of draw
      - [ ] else notify both of winner
- [ ] commands
  - [x] ?tictactoe [ ] functional
    - [ ] store to separate server app via tictactoeServer.py functions
    - [ ] stretch goal: database
      - [ ] send private message from bot inviting player
    - [x] ?accept [ ] functional
      - [ ] if gameID['game'].active, send board to initiator with not of cur_player
    - [x] ?deny (for denying request) [ ] functional
      - [ ] else grab players[0] and send a notification of denial
    - [x] ?move row column gameID [ ] functional
    - [ ] notify opponent of game update
    - [x] ?quit [ ] functional
      - [ ] send game's board to both
      - [ ] notify both game has been ended by author
- [ ] Store Persistent Data TODO: determine best method using a server to store data
  - [ ] call to local server
  - [ ] pull updated dictionary from text file
  - [ ] look for game
    - [ ] FIXME: using text file, TicTacToe object details won't be stored...
- [ ] Testing:
  - [ ] dpytest
  - [ ] [unittest](https://docs.python.org/3/library/unittest.html)
- [ ] Automate:
  - [ ] automate testing
    - [ ] games
    - [ ] bot
  - [ ] if passed, deploy
  - [ ] else log failed tests

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
- [ ] commands
  - [x] ?tictactoe [ ] functional
    - [x] ?challenge [x] functional
      - [x] player1: ?tictactoe challenge username
        - [x] verify 2 users are not already associated with a current gameID
        - [x] store gameID: { players: [username, initiator], game: TicTacToe()}
          - [x] initiates game start
      - [ ] send private message from bot inviting player
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
    - [x] ?move row column gameID [ ] functional
      - [x] if gameID specified use that game
      - [x] else find gameID and display appropriate command
      - [x] parse row and column into integers
        - [x] check in bounds & selected place is none
          - [x] if issue display error
      - [x] update board via t3.make_move(row, column)
    - [x] ?quit [ ] functional
      - [x] find gameID
      - [x] del gameID['game]
