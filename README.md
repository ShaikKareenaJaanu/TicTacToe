# TIC_TAC_TOE

## OVERVIEW

This documentation provides a comprehensive guide to the Tic-Tac-Toe game implemented using the Tkinter library in Python. The game allows two players to compete against each other, keeping track of scores and rounds.

## Table of Contents

* Features<br>
* Code Structure <br>
* Function Descriptions <br>
* Global Variables <br>
* GUI Components <br>
* Conclusion<br>


## FEATURES


* Players can enter their names and specify the number of rounds. <br>
* The game tracks scores and announces the winner after each round. <br>
* The game concludes after the specified number of rounds, displaying final scores. <br>


* Player Name Input and Round Specification :<br>

    Players can enter their names and specify the number of rounds they wish to play at the start of the game.
  The game prompts for Player 1's name (X) and Player 2's name (O) or allows Player 2 to be an AI.<br>

* Dynamic Game Board :<br>

    A 3x3 grid of buttons is created dynamically for the Tic-Tac-Toe game.
   Players click on the buttons to place their marks (X or O).<br> 

* Score Tracking :<br>

     The game keeps track of scores for both players throughout the rounds.
  Scores are displayed and updated after each round.<br>

* Winner Announcement :<br>

     After each round, the game checks for a winner or a draw.
  A message box displays the winner's name or announces a draw.<br>

* Game Conclusion :<br>

     The game automatically concludes after the specified number of rounds.
  Final scores are displayed in a message box at the end of the game.<br>

* Highlight Winning Line :<br>

     When a player wins, the winning line (row, column, or diagonal) is visually highlighted in green.
   This feature enhances the visual feedback for players.<br> 

* User Interface Elements :<br>

     Labels are used to display player scores and the current player's turn.
   The interface is designed to be intuitive and easy to navigate.<br>

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


* buttons:<br>
   List to hold button widgets for the Tic-Tac-Toe grid. <br>
* current_player:<br>
Tracks whose turn it is ("X" or "O"). <br>
* winner:<br>
 Stores the winner of the game. <br>
* scores:<br>
 List to keep track of scores for both players.<br>
* rounds_played:<br>
 Counter for the number of rounds played. <br>
* player1, player2:<br>
 Strings to store the names of the players. <br>
* total_rounds:<br>
 Integer to specify how many rounds will be played.<br>


## GUI COMPONNTS <br>


LABLES: Display player scores and whose turn it is. <br>
BUTTONS: Represent the Tic-Tac-Toe grid, allowing players to make their moves. <br>


## Conclusion
This Tic-Tac-Toe game provides a comprehensive and engaging experience for players, with features that enhance gameplay, track progress, and allow for both competitive and casual play. The implementation is designed to be user-friendly, making it accessible for players of all ages.
