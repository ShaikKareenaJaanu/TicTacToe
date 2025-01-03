import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []  
current_player = "X"
winner = None
scores = [0, 0]  
rounds_played = 0
player1 = ""
player2 = ""
total_rounds = 0

def get_player_info()->str:
    global player1, player2, total_rounds
    player1 = simpledialog.askstring("Player 1", "Enter name for Player 1 (X):")
    player2 = simpledialog.askstring("Player 2", "Enter name for Player 2 (O):")
    total_rounds = simpledialog.askinteger("Rounds", "Enter number of rounds to play:")
    create_buttons()
    reset_game()
    label2.config(text=f"{player1} vs {player2}")

def create_buttons()->None:
    global buttons
    for i in range(9):
        button = tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
                           command=lambda i=i: button_click(i))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)

def check_winner()->None:
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = buttons[combo[0]]["text"]
            messagebox.showinfo("Tic-Tac-Toe", f"{player1 if winner == 'X' else player2} wins!")
            update_score(winner)
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        update_score("Draw")

def update_score(winner)->int:
    global rounds_played
    if winner == "X":
        scores[0] += 1
    elif winner == "O":
        scores[1] += 1
    rounds_played += 1
    update_score_labels()
    if rounds_played < total_rounds:
        reset_game()
    else:
        messagebox.showinfo("Game Over", f"Final Scores:\n{player1}: {scores[0]}\n{player2}: {scores[1]}")
        root.quit()

def update_score_labels()->int:
    score_label1.config(text=f"{player1}: {scores[0]}")
    score_label2.config(text=f"{player2}: {scores[1]}")

def reset_game()->None:
    global winner, current_player  
    winner = None
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    current_player = "X" if rounds_played % 2 == 0 else "O"
    label.config(text=f"{player1 if current_player == 'X' else player2}'s turn")

def button_click(index)->None:
    if buttons[index]["text"] == "" and winner is None:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player()->str:
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"{player1 if current_player == 'X' else player2}'s turn")

# Labels for displaying scores
score_label1 = tk.Label(root, text="", font=("normal", 16))
score_label1.grid(row=5, column=0)

score_label2 = tk.Label(root, text="", font=("normal", 16))
score_label2.grid(row=5, column=2)

label = tk.Label(root, text="", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

label2 = tk.Label(root, text="", font=("normal", 16))
label2.grid(row=4, column=0, columnspan=3)

get_player_info()

root.mainloop()
