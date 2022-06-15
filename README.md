# ChantelM-project0
Project 0: Server Game

## Modules Used:
[python-dotenv](https://pypi.org/project/python-dotenv/)
[Discord Developer Portal](https://discord.com/developers/docs/intro)
[discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Discord API](https://discordpy.readthedocs.io/en/stable/api.html)
[dpytest](https://dpytest.readthedocs.io/en/latest/)

## TODO:
- [ ] discord bot initial deploy
  - [ ] read message
  - [ ] assign tic-tac-toe command
- [x] tic-tac-toe
  - [x] create class
    - [x] start game
    - [x] stop game
    - [x] track game play
- [ ] discord bot game channel creation
  - [ ] first player !tic-tac-toe second_player_name
    - [ ] create channel
    - [ ] invite second player
  - [ ] second player accepts
    - [ ] initiates game start with subcommand to make a move
  - [ ] game cycles through
- [ ] subcommands
  - [ ] !display_board
  - [ ] !quit
  - [ ] !denied 
  - [ ] !accept
  - [ ] !enter_move
  - [ ] !start
- [ ] Store Persistent Data TODO: determine best method using a server to store data (webhook or websocket?)
  - [ ] channel name
    - [ ] user0 and user1 associated discord user names
    - [ ] tic-tac-toe instance
- [ ] Testing:
  - [ ] dpytest
  - [ ] [unittest](https://docs.python.org/3/library/unittest.html)
- [ ] Automate:
  - [ ] FIXME: figure out!
- [ ] Adjust Bot permissions
