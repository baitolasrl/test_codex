from js import document, window
from random import randint

canvas = document.getElementById('game')
ctx = canvas.getContext('2d')

grid_size = 20
cols = canvas.width // grid_size
rows = canvas.height // grid_size

snake = [[cols // 2, rows // 2]]
direction = [1, 0]
apple = [randint(0, cols - 1), randint(0, rows - 1)]


def draw():
    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    ctx.fillStyle = 'red'
    ctx.fillRect(apple[0] * grid_size, apple[1] * grid_size, grid_size, grid_size)

    ctx.fillStyle = 'green'
    for x, y in snake:
        ctx.fillRect(x * grid_size, y * grid_size, grid_size, grid_size)


def move(*args):
    head_x, head_y = snake[0]
    new_head = [head_x + direction[0], head_y + direction[1]]

    if (
        new_head[0] < 0 or new_head[0] >= cols or
        new_head[1] < 0 or new_head[1] >= rows or
        new_head in snake
    ):
        window.clearInterval(interval_id)
        window.alert('Game Over!')
        return

    snake.insert(0, new_head)

    if new_head == apple:
        apple[0] = randint(0, cols - 1)
        apple[1] = randint(0, rows - 1)
    else:
        snake.pop()

    draw()


def keydown(event):
    global direction
    key = event.key
    if key == 'ArrowUp' and direction != [0, 1]:
        direction = [0, -1]
    elif key == 'ArrowDown' and direction != [0, -1]:
        direction = [0, 1]
    elif key == 'ArrowLeft' and direction != [1, 0]:
        direction = [-1, 0]
    elif key == 'ArrowRight' and direction != [-1, 0]:
        direction = [1, 0]


document.addEventListener('keydown', keydown)

draw()
interval_id = window.setInterval(move, 150)

