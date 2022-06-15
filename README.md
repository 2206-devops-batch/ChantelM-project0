# ChantelM-project0
Project 0: Server Game

## Modules Used:
[python-dotenv](https://pypi.org/project/python-dotenv/)
[Discord Developer Portal](https://discord.com/developers/docs/intro)
[discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Discord API](https://discordpy.readthedocs.io/en/stable/api.html)
[dpytest](https://dpytest.readthedocs.io/en/latest/)

## TODO:
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
      - [x] __str__ to display board as TTT method
- [ ] discord bot deploy with game
  - [ ] initial command functions
  - [ ] game Loop
    - [ ] wait for command
    - [ ] if gameID['game'].active
      - [ ]  if correct player, allow move
      - [ ]  else notify it is not there turn
    - [ ] if not gameID['game'].active
      - [ ] notify both of board
      - [ ] if not gameID['game'].winner, notify both of draw
      - [ ] else notify both of winner
- [ ] commands
  - [x] ?tictactoe [ ] functional
    - [x] ?challenge [ ] functional
      - [ ] first player ?tictactoe challenge username
        - [ ] verify 2 users are not already associated with a current gameID
        - [ ] store gameID: { players: [initiator, username], game: None}
          - [ ]  FIXME: figure out storing (server <-> .txt ?)
          - [ ]  stretch goal: database
        - [ ] send private message from bot inviting player
    - [x] ?accept [ ] functional 
      - [ ] second player ?tictactoe accept row column
        - [ ] initiates game start 
          - [ ] find the appropriate gameID with username in players & game=None
          - [ ] update associated gameID['game']:
            - [ ] t3 = TicTacToe('x', 'o')
            - [ ] t3.start_game()
            - [ ] t3.make_move(row, column)
            - [ ] via gameID['game'].move(row, column)
          - [ ] if gameID['game'].active, send board to initiator
    - [x] ?deny (for denying request) [ ] functional
      - [ ] second player ?tictactoe deny
      - [ ] find game with author as player
        - [ ] if more than one gameID['game] is None with author in players:
          - [ ] list appropriate gameIDs (with challenger) and display how to specify
        - [ ] else grab players[0] and send a notification of denial
    - [x] ?move row column gameID [ ] functional
      - [ ] if gameID specified use that game 
      - [ ] else find gameID and display appropriate command
      - [ ] parse row and column into integers
        - [ ] check in bounds & selected place is none
          - [ ] if issue display error
      - [ ] update board via t3.make_move(row, column)
      - [ ] notify opponent of game update
    - [x] ?quit
      - [ ] find gameID
      - [ ] send game's board to both
      - [ ] gameID['game].end_game()
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
    - [ ] if passed, deploy
    - [ ] else log failed tests
