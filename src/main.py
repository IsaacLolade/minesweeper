from tkinter import *
from functools import partial
from pynput import mouse
import random


def create_game_table(game_dict: dict) -> None:
    global window
    for r_key, r_val in game_dict.items():
        for c_key, c_val in r_val.items():
            globals()[f"btn_{r_key-c_key}"] = StringVar(window)
            globals()[f"btn_{r_key-c_key}"].set(c_val[0])
            # textvariable=globals()[f"btn_{r_key-c_key}"] -> Button textvariable
            Button(window, image=c_val[1]).grid(
                row=r_key+1, column=c_key)


if __name__ == "__main__":

    # Define window element
    window = Tk()

    # Add title and not resizable
    window.title("MinesWeeper Game")
    # window.geometry("300x300")
    window.resizable(False, False)

    remaining_mines = StringVar(window)
    remaining_mines.set(10)

    game = {}
    # * This is for my personal folder open on VSCode (on Programming subject directory)
    def_img = PhotoImage(
        file="01 Python/Actividades/MinesWeeper/src/icons/png/24/tile.png")

    restart_img = PhotoImage(
        file="01 Python/Actividades/MinesWeeper/src/icons/png/24/smiley.png")

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

    # Label(window, text="GAME TOP BAR").grid(
    #     row=0, column=0, columnspan=8, pady=10)

    Label(window, textvariable=remaining_mines, justify=CENTER,
          font=('KacstDigital', 20), bg='black', fg='red').grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    Button(window, image=restart_img).grid(row=0, column=3, columnspan=2)

    Label(window, textvariable=remaining_mines, justify=CENTER,
          font=('KacstDigital', 20), bg='black', fg='red').grid(row=0, column=5, columnspan=2, padx=10, pady=10)

    create_game_table(game)

    window.mainloop()
