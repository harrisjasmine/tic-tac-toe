## Tic-Tac-Toe

Tic-Tac-Toe is a game where a player(or multiple players)can play against each other or the computer by providing their input via the keyboard. Each player is assigned a character, such as "X" for player 1 and "O" for player 2, to be marked on the board. A player wins the game by successfully placing their character horizontally, vertically, or diagonally across the board. When a player satisfies these conditions, a winner will be declared. Otherwise, a draw will be declared. If you are playing as 'multiplayer', a scoreboard containing the top 5 scorers will appear followed by a prompt to play again. 'Computer' gameplay will simply prompt to play again. 

## Motivation

This project was completed as a code sample for promotion to level 3 in the REACH apprenticeship program.

## Tech/framework used

* Python
* Pytest
* Unittest

## Features

* The user can determine size of the board via input
* Option for multiplayer game
* Option to play against the computer
* Scoreboard of top 5 scoreers displayer after 'multiplayer' gameplay
* 'Play again' prompt after each game
*  X, Y coordinate guide displayed with board

## Tests

Tests were created using the Pytest and Unittest frameworks

tests can be run using 'pytest'

## How to use?

* Enter the game by using the command 'python game.py'
* Prompt for 'multiplayer' or 'computer' appears, enter 'm' or 'c' for either
* Board size required prompt appears, enter integer for desired board size
* Prompt to enter player(s) name appear
* Board is drawn onto the screen
* Each player enters their move via X, Y coordinates
* Play again prompt appears, after a winner or draw is declared

## Installation

* Clone the repository 
* Run the game using command 'python game.py'
