# Minesweeper Game

## DAM collaboration project - Python 3 and Tkinter GUI

This project was a proposal in class after finishing the Python course.

![Wikipedia-MinesWeeper](https://upload.wikimedia.org/wikipedia/commons/6/6c/Minesweeper%28game%29.jpg)

[Wikipedia MinesWeeper ](<https://en.wikipedia.org/wiki/Minesweeper_(video_game)>)

> Beginner is usually on an 8x8 or 9x9 board containing 10 mines

As Wikipedia says, on a 8x8 or 9x9 table, there are 10 mines in total, so we decided to set this as a start point for the project (maybe later we decide to expand it).

### Modules used

-  **tkinter**: For GUI.
-  **functools**: For using params in buttons <kbd>command</kbd> attribute. We only need <kbd>partial</kbd> method.
-  **random**: Generate random coordinates to place mines at the start.
-  **pynput**: Register mouse clicks and what click (right|left)

```python
	from tkinter import *
	from functools import partial
	from pynput import mouse
	import random
```

`pynput` is not a common library in Python3, so we need to install it.

```bash
	$ pip install pynput
```

<br>
Maybe is not the best GUI manager but we used Tkinter because is the one they've taught us on class. Also is very easy to use and has simple syntax.

## Authors

-  [Carlos Sánchez Recio](https://github.com/CharlyMech)
-  [Marc Albert Seguí Olmos](https://github.com/MarcASO1560)
