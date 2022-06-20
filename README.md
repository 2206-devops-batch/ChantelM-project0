# ChantelM-project0

Discord Bot for playing Tic-Tac-Toe with a
Client-Server LAN to store game objects

- [ChantelM-project0](#chantelm-project0)
- [About the Project](#about-the-project)
  - [Purpose & Goal](#purpose--goal)
  - [Frameworks](#frameworks)
  - [Project Structure](#project-structure)
- [Setup & Deployment](#setup--deployment)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Deployment](#deployment)
- [Usage](#usage)

# About the Project

![Example game_bot game of Tic Tac Toe](/images/game_bot_autoplay.png)

## Purpose & Goal

Bots on Discord are known as a useful tool for automating tasks. To reduce the
robotic feel of automated introductions, game_bot breaks the ice by facilitating
a game of TicTacToe between 2 server members.

The created Discord bot (game_bot) communicates with a server over a local area network.
The server provides persistent game data storage by maintaining all instances of a game
along with associated players' data.

## Frameworks

Below is a list of frameworks used in this project.

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
  - [Bot Commands Framework](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Project Structure

![File Structure](/images/file_structue.png)

# Setup & Deployment

## Prerequisites

- [Discord Developer Portal Application](https://discord.com/developers/docs/getting-started)
  - Application token
- Remember to [invite the bot to a server](https://discord.com/developers/docs/getting-started#configuring-a-bot)

## Setup

1. Use your application's token and fill in the specified items in [ExampleEnv.txt](ExampleEnv.txt)
2. Rename ExampleEnv.txt to .env

## Deployment

- app.sh
- termination instructions

# Usage

- challenge
- deny
- accept
- move
- quit
- automate
