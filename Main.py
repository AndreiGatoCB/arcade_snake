from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Snake de Gato")
pantalla.tracer(0)

snake = Snake()
comida = Food()
puntaje = Scoreboard()
pantalla.listen()
pantalla.onkey(snake.up, "Up")
pantalla.onkey(snake.down, "Down")
pantalla.onkey(snake.left, "Left")
pantalla.onkey(snake.right, "Right")

jugando = True
while jugando:
    pantalla.update()
    time.sleep(0.1)
    snake.move()

    if snake.cabeza.distance(comida) < 15:
        comida.refresh()
        snake.extender()
        puntaje.sumar_puntaje()

    if snake.cabeza.xcor() > 280 or snake.cabeza.xcor() < -300 or \
            snake.cabeza.ycor() > 300 or snake.cabeza.ycor() < -290:
        puntaje.reset()
        snake.reset()

    for seg in snake.secciones[1:]:
        if snake.cabeza.distance(seg) < 10:
            puntaje.reset()
            snake.reset()

pantalla.exitonclick()
