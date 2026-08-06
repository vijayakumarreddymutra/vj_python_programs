import tkinter as tk
from tkinter import messagebox

# -------------------------
# Window
# -------------------------
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("360x420")
root.resizable(False, False)

current_player = "X"
board = [""] * 9
buttons = []

# -------------------------
# Check Winner
# -------------------------
def check_winner():
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


# -------------------------
# Button Click
# -------------------------
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player

        result = check_winner()

        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
            return

        elif result:
            messagebox.showinfo("Winner", f"Player {result} Wins!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s Turn")


# -------------------------
# Reset Game
# -------------------------
def reset_game():
    global current_player

    current_player = "X"

    for i in range(9):
        board[i] = ""
        buttons[i]["text"] = ""

    status_label.config(text="Player X's Turn")


# -------------------------
# Status Label
# -------------------------
status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 18, "bold")
)
status_label.pack(pady=10)

# -------------------------
# Game Board
# -------------------------
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

# -------------------------
# Restart Button
# -------------------------
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    command=reset_game
)
restart_btn.pack(pady=20)

root.mainloop()