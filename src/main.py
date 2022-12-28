from tkinter import *
from functools import partial
from pynput import mouse
from time import time
import random


def count_mines(game_dict: dict) -> int:
    mines_count = 0
    for rv in game_dict.values():
        for cv in rv.values():
            if cv[0] == 'm':
                mines_count += 1

    return mines_count


def put_mines(game_dict: dict) -> None:
    mines_count = count_mines(game_dict)
    while mines_count < 10:
        rand_x = random.randint(0, 7)
        rand_y = random.randint(0, 7)

        game_dict[rand_x][rand_y][0] = 'm'

    # return game_dict


def create_game_table(game_dict: dict) -> None:
    global window
    for r_key, r_val in game_dict.items():
        for c_key, c_val in r_val.items():
            globals()[f"btn_{r_key-c_key}"] = StringVar(window)
            globals()[f"btn_{r_key-c_key}"].set(c_val[0])
            # textvariable=globals()[f"btn_{r_key-c_key}"] -> Button textvariable
            Button(window, image=c_val[1]).grid(
                row=r_key+1, column=c_key)


def timer():
    global init_seconds, stop

    # sleep(1)
    seconds = round(time()) - init_seconds

    if stop == 0:
        lbl = Label(window, text=f"{seconds}", justify=CENTER,
                    font=('KacstDigital', 20), bg='black', fg='red')
        lbl.after(200, timer)
        lbl.grid(row=0, column=5, columnspan=2, padx=10, pady=10)


def restart():
    global stop
    stop = 1
    seconds.set(0)
    stop = 0


if __name__ == "__main__":

    # Define window element
    window = Tk()

    # Add title and not resizable
    window.title("MinesWeeper Game")
    # window.geometry("300x300")
    window.resizable(False, False)

    remaining_mines = StringVar(window)
    remaining_mines.set(10)

    init_seconds = round(time())
    stop = 0

    timer()

    game = {}
    # * This is for my personal folder open on VSCode (on Programming subject directory)
    def_img = PhotoImage(
        file="01 Python/Actividades/MinesWeeper/src/icons/24/tile.png")

    restart_img = PhotoImage(
        file="01 Python/Actividades/MinesWeeper/src/icons/24/smiley.png")

    # * This is the path for the standalone project
    # def_img = PhotoImage(
    #     file="./src/icons/png/24/tile.png")
    # restart_img = PhotoImage(
    #     file="./src/icons/png/24/smiley.png")

    # Remember that for now it's a 8x8 game
    for r in range(8):
        game[r] = {}
        for c in range(8):
            game[r][c] = ["0", def_img]

    Label(window, textvariable=remaining_mines, justify=CENTER,
          font=('KacstDigital', 20), bg='black', fg='red').grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    restart_btn = Button(window, image=restart_img, command=restart).grid(
        row=0, column=3, columnspan=2)

    # Label(window, textvariable=seconds, justify=CENTER,
    #       font=('KacstDigital', 20), bg='black', fg='red').grid(row=0, column=5, columnspan=2, padx=10, pady=10)

    create_game_table(game)

    window.mainloop()
