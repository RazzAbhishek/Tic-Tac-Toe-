import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#2c3e50")
        
        # Game variables
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.game_active = True
        
        # Style configuration
        self.button_font = ("Helvetica", 20, "bold")
        self.button_width = 6
        self.button_height = 3
        
        # Create game board
        self.create_board()
        
        # Create status label
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Create reset button
        self.reset_button = tk.Button(
            self.window,
            text="Reset Game",
            font=("Helvetica", 12),
            bg="#e74c3c",
            fg="white",
            command=self.reset_game,
            width=15,
            height=2
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)
        
    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=self.button_font,
                    bg="#34495e",
                    fg="white",
                    width=self.button_width,
                    height=self.button_height,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
    
    def make_move(self, row, col):
        if not self.game_active:
            return
            
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                bg="#3498db" if self.current_player == "X" else "#2ecc71"
            )
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_active = False
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.game_active = False
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
                
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
                
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
            
        return False
    
    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.game_active = True
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        
        for button in self.buttons:
            button.config(text="", bg="#34495e")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run() 