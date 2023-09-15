from turtle import *
from freegames import line

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    pencolor("red")
    width(2)
    center_x = x + 65  # Calcular el centro en el eje x
    center_y = y + 65  # Calcular el centro en el eje y
    up()
    goto(center_x - 45, center_y - 45)
    down()
    goto(center_x + 45, center_y + 45)
    up()
    goto(center_x - 45, center_y + 45)
    down()
    goto(center_x + 45, center_y - 45)

def drawo(x, y):
    """Draw O player."""
    pencolor("blue")
    up()
    goto(x + 67, y + 5)
    down()
    circle(55)

# Crear una matriz para representar el estado del tablero
tablero = [[' ' for _ in range(3)] for _ in range(3)]

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = int((x + 200) // 133)
    y = int((y + 200) // 133)
    player = state['player']

    # Verificar si la casilla ya está ocupada
    if 0 <= x < 3 and 0 <= y < 3 and tablero[y][x] == ' ':
        draw = players[player]
        draw(x * 133 - 200, y * 133 - 200)
        update()

        # Marcar la casilla como ocupada con el jugador actual
        tablero[y][x] = 'X' if player == 0 else 'O'

        # Cambiar al siguiente jugador
        state['player'] = not player
    else:
        print("Esta casilla ya está ocupada o no es válida. Elige otra.")

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
