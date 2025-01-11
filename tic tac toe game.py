import tkinter as tk
import tkinter.messagebox
import random

root = tk.Tk()
root.title("tic tac toe game")
root.geometry("230x260")


if random.randint(1,2) == 1:
    playerS = "X"
    computerS = "O"
else:
    playerS = "O"
    computerS = "X"

def XO2(button, index):
    global ap
    if button in ap:
        button.config(text = playerS)
        ap.remove(button)
        win()
        button = random.choice(ap)
        button.config(text = computerS)
        ap.remove(button)
        win()

def win():
    winc = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6),(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    for i in range(8):
        if nbv[winc[i][0]]["text"] == playerS and nbv[winc[i][1]]["text"] == playerS and nbv[winc[i][2]]["text"] == playerS:
            tkinter.messagebox.showinfo("Player Won!", "You have won the game!")
            break
        elif nbv[winc[i][0]]["text"] == computerS and nbv[winc[i][1]]["text"] == computerS and nbv[winc[i][2]]["text"] == computerS:
            tkinter.messagebox.showinfo("Computer Won!", "You have lost the game!")
            break
        elif len(ap) == 0:
            tkinter.messagebox.showinfo("Tie game!", "The game is a tie!")
            break
player_label = tk.Label(root, text = "Player = " + playerS)
player_label.grid(row = 1, column = 1)
computer_label = tk.Label(root, text = "Computer = " + computerS)
computer_label.grid(row = 2, column = 1)

grid1 = tk.Button(root, width = 9, height = 4, command = lambda:XO2(grid1, 0))
grid1.grid(row = 3, column = 1)
grid2 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid2, 1))
grid2.grid(row = 3, column = 2)
grid3 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid3, 2))
grid3.grid(row = 3, column = 3)
grid4 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid4, 3))
grid4.grid(row = 4, column = 1)
grid5 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid5, 4))
grid5.grid(row = 4, column = 2)
grid6 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid6, 5))
grid6.grid(row = 4, column = 3)
grid7 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid7, 6))
grid7.grid(row = 5, column = 1)
grid8 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid8, 7))
grid8.grid(row = 5, column = 2)
grid9 = tk.Button(root, width = 9, height =4, command = lambda:XO2(grid9, 8))
grid9.grid(row = 5, column = 3)

ap = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]
nbv = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]

root.mainloop()