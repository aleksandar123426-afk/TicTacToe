import tkinter

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[None for _ in range(3)] for _ in range(3)]
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"
turns = 0
game_over = False


def set_tile(row, column):
    global curr_player
    if game_over or board[row][column]["text"] != "":
        return
    board[row][column]["text"] = curr_player
    curr_player = playerO if curr_player == playerX else playerX
    label.config(text=curr_player + "'s turn")
    check_winner()


def check_winner():
    global turns, game_over
    turns += 1
    lines = [
        [(r, c) for c in range(3)] for r in range(3)
    ] + [
        [(r, c) for r in range(3)] for c in range(3)
    ] + [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
    for line in lines:
        values = [board[r][c]["text"] for r, c in line]
        if values[0] and values.count(values[0]) == 3:
            label.config(text=values[0] + " is the winner!", foreground=color_yellow)
            for r, c in line:
                board[r][c].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)


def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)


window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame, text="", font=("Consolas", 50, "bold"),
            background=color_gray, foreground=color_blue, width=4, height=1,
            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20),
                        background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{window_width}x{window_height}+{(screen_width - window_width) // 2}+{(screen_height - window_height) // 2}")
window.mainloop()
                                                    
                                