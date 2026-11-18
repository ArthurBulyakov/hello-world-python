import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        
        # Заголовок
        self.label = tk.Label(
            root, 
            text="Ход: X", 
            font=("Arial", 20, "bold"),
            bg="#2c3e50", 
            fg="#ecf0f1"
        )
        self.label.pack(pady=20)
        
        # Рамка для поля
        frame = tk.Frame(root, bg="#2c3e50")
        frame.pack()
        
        # Создаём кнопки 3x3
        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Arial", 28, "bold"),
                width=4,
                height=2,
                bg="#34495e",
                fg="#ecf0f1",
                activebackground="#3d566e",
                relief="flat",
                command=lambda idx=i: self.on_click(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
        
        # Кнопка новой игры
        restart_btn = tk.Button(
            root,
            text="Новая игра",
            font=("Arial", 14),
            bg="#27ae60",
            fg="white",
            activebackground="#219a52",
            relief="flat",
            padx=20,
            pady=10,
            command=self.restart
        )
        restart_btn.pack(pady=20)
    
    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                fg="#e74c3c" if self.current_player == "X" else "#3498db"
            )
            
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.label.config(text=f"Победил: {self.current_player}")
            elif "" not in self.board:
                messagebox.showinfo("Ничья", "Ничья!")
                self.label.config(text="Ничья!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Ход: {self.current_player}")
    
    def check_winner(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),  # горизонтали
            (0,3,6), (1,4,7), (2,5,8),  # вертикали
            (0,4,8), (2,4,6)            # диагонали
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                # Подсветка выигрышной линии
                self.buttons[a].config(bg="#f1c40f")
                self.buttons[b].config(bg="#f1c40f")
                self.buttons[c].config(bg="#f1c40f")
                return True
        return False
    
    def restart(self):
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.label.config(text="Ход: X")
        for btn in self.buttons:
            btn.config(text="", bg="#34495e")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
