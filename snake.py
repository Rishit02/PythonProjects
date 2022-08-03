import curses
from curses import *
from random import *
import time

s = curses.initscr()    # initializes a new window for capturing key presses
curs_set(0) # Keep the cursor on the top left
sh, sw = s.getmaxyx() # Get the boundaries of the screen
w = newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100) # 100 ms
score = 0 # Initialize the score

snk_x = sw/4
snk_y = sh/2
# Snake is a 2D array
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = KEY_RIGHT

"""
The next part is important as it is the game loop
"""

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Conditions for loss
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        print(f"Your score is: {score}")
        time.sleep(5)
        endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # Conditions for movement depending on key presses
    if key == KEY_DOWN:
        new_head[0] += 1
    if key == KEY_UP:
        new_head[0] -= 1
    if key == KEY_LEFT:
        new_head[1] -= 1
    if key == KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food: # If the front head of the snake is at the same location at the food
        score += 1
        food = None # The food disapears
        while food is None:
            nf = [
                randint(1, sh-1),
                randint(1, sw-1)
            ] # The food reapears in a random location within the screeen
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
