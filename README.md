#TIC_TAC_TOE 

##Overview
This documentation provides a comprehensive guide to the Tic-Tac-Toe game implemented using the Tkinter library in Python. The game allows two players to compete against each other, keeping track of scores and rounds.

##Table of Contents
*Installation
*Usage
*Code Structure
*Function Descriptions
*Global Variables
*GUI Components
*Features

##Code Structure
The code is structured into several key components:

IMPORTS: Necessary modules from Tkinter for GUI creation and dialog handling.
GLOBAL VARIABLES: Variables to manage game state, player information, and scores.
FUNCTIONS: Defined to handle game logic, user interactions, and GUI updates.
GUI COMPONENTS: Labels and buttons to create the game interface.

##Function Descriptions
get_player_info() -> str
Prompts players for their names and the total number of rounds to play. Initializes the game by creating buttons and resetting the game state.

create_buttons() -> None
Creates a 3x3 grid of buttons for the Tic-Tac-Toe game and adds them to the GUI.

check_winner() -> None
Checks for a winning combination or a draw after each move. Updates the UI to indicate the winner or a draw.

update_score(winner) -> int
Updates the scores based on the winner of the round. Checks if the game should continue or end after the specified number of rounds.

update_score_labels() -> None
Updates the displayed scores for both players on the GUI.

reset_game() -> None
Resets the game state for a new round, clearing the buttons and updating the current player.

button_click(index) -> None
Handles the button click event, updates the button text, checks for a winner, and toggles the current player.

toggle_player() -> str
Switches the current player and updates the turn label on the GUI.

##Global Variables
buttons: List to hold button widgets for the Tic-Tac-Toe grid.
current_player: Tracks whose turn it is ("X" or "O").
winner: Stores the winner of the game.
scores: List to keep track of scores for both players.
rounds_played: Counter for the number of rounds played.
player1, player2: Strings to store the names of the players.
total_rounds: Integer to specify how many rounds will be played.

GUI Components
Labels: Display player scores and whose turn it is.
Buttons: Represent the Tic-Tac-Toe grid, allowing players to make their moves.

##Features
Players can enter their names and specify the number of rounds.
The game tracks scores and announces the winner after each round.
The game concludes after the specified number of rounds, displaying final scores.
Potential Improvements

