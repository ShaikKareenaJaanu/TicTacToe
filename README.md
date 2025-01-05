# TIC_TAC_TOE

## OVERVIEW

This documentation provides a comprehensive guide to the Tic-Tac-Toe game implemented using the Tkinter library in Python. The game allows two players to compete against each other, keeping track of scores and rounds.

## Table of Contents

* Installation <br>
* Usage <br>
* Code Structure <br>
* Function Descriptions <br>
* Global Variables <br>
* GUI Components <br>
* Features <br>

## CODE STRUCTURE <br>


The code is structured into several key components: <br>

IMPORTS:<br>
Necessary modules from Tkinter for GUI creation and dialog handling. <br>
GLOBAL VARIABLES: <br>
Variables to manage game state, player information, and scores. <br>
FUNCTIONS:<br>
Defined to handle game logic, user interactions, and GUI updates. <br>
GUI COMPONENTS:<br>
Labels and buttons to create the game interface. <br>


## Function Descriptions


* get_player_info() -> str <br>
Prompts players for their names and the total number of rounds to play. Initializes the game by creating buttons and resetting the game state. <br> 

* create_buttons() -> None <br>
Creates a 3x3 grid of buttons for the Tic-Tac-Toe game and adds them to the GUI. <br>

* check_winner() -> None <br>
Checks for a winning combination or a draw after each move. Updates the UI to indicate the winner or a draw. <br>

* update_score(winner) -> int <br>
Updates the scores based on the winner of the round. Checks if the game should continue or end after the specified number of rounds. <br>

* update_score_labels() -> None <br>
Updates the displayed scores for both players on the GUI.<br>

* reset_game() -> None <br>
Resets the game state for a new round, clearing the buttons and updating the current player. <br>

* button_click(index) -> None <br>
Handles the button click event, updates the button text, checks for a winner, and toggles the current player. <br>

* toggle_player() -> str <br>
Switches the current player and updates the turn label on the GUI. <br>


## Global Variables <br>


buttons: List to hold button widgets for the Tic-Tac-Toe grid. <br>
current_player: Tracks whose turn it is ("X" or "O"). <br>
winner: Stores the winner of the game. <br>
scores: List to keep track of scores for both players.<br>
rounds_played: Counter for the number of rounds played. <br>
player1, player2: Strings to store the names of the players. <br>
total_rounds: Integer to specify how many rounds will be played.<br>


## GUI COMPONNTS <br>


LABLES: Display player scores and whose turn it is. <br>
BUTTONS: Represent the Tic-Tac-Toe grid, allowing players to make their moves. <br>


## FEATURES


* Players can enter their names and specify the number of rounds. <br>
* The game tracks scores and announces the winner after each round. <br>
* The game concludes after the specified number of rounds, displaying final scores. <br>


