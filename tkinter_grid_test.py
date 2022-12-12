import tkinter as tk


# Define root element
window = tk.Tk()

# Add title and window dimensions
window.title("MinesWeeper Game")
window.geometry('350x400+50+50')
# Don't let the user change the window size
window.resizable(False, False)

# Change window icon
#! Not working!
# window.iconbitmap('./icons/tile4.ico')


def doing_nothing():
    # test function
    print("One button pressed")


# Frame for title
title_frame = tk.Frame(window)
title_frame.pack(side=tk.TOP)

title = tk.Label(title_frame, text='MinesWeeper GAME')
space = tk.Label(title_frame, text='')

title.pack()
space.pack()

# Frame for the buttons table
main_frame = tk.Frame(window, width=350)
main_frame.pack()

# Generate table
for r in range(9):
    globals()['frame%s' % r] = tk.Frame(main_frame)
    globals()['frame%s' % r].pack()
    for c in range(9):
        globals()['btn%s' % c] = tk.Button(globals()['frame%s' % r], image=tk.PhotoImage(
            file='icons/png/16/flag.png'), command=doing_nothing)
        globals()['btn%s' % c].pack(side=tk.RIGHT)


# Add window element to main loop -> window loop
window.mainloop()
