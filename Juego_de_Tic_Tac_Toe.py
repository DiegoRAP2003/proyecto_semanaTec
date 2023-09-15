"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 100, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    pencolor("red")
    line(x, y, x + 100, y + 100)
    line(x, y + 100, x + 100, y)


def drawo(x, y):
    """Draw O player."""
    pencolor("blue")
    up()
    goto(x + 67, y + 5)
    down()
    circle(50)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


tablero = [['' for _ in range(3)] for _ in range(3)]


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""

    x = floor(x)
    y = floor(y)
    player = state['player']
    if tablero[y][x] == '':
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        tablero[y][x] = 'X' if player == 0 else 'O'
    else:
        print("Esta casilla ya está ocupada. Elige otra.")


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()