from turtle import Turtle, Screen

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
MOVERSE = 20
PANTALLA = Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.secciones = []
        self.crear_snake()
        self.cabeza = self.secciones[0]

    def crear_snake(self):
        for posicion in POSICIONES_INICIALES:
            self.agregar_segmento(posicion)

    def agregar_segmento(self, posicion):
        seccion_nueva = Turtle(shape="square")
        seccion_nueva.color("white")
        seccion_nueva.penup()
        seccion_nueva.goto(posicion)
        self.secciones.append(seccion_nueva)

    def extender(self):
        self.agregar_segmento(self.secciones[-1].position())

    def move(self):
        for sec_num in range(len(self.secciones) - 1, 0, -1):
            x_n = self.secciones[sec_num - 1].xcor()
            y_n = self.secciones[sec_num - 1].ycor()
            self.secciones[sec_num].goto(x_n, y_n)
        self.cabeza.forward(MOVERSE)

    def up(self):
        if self.cabeza.heading() != DOWN:
            self.cabeza.setheading(UP)

    def down(self):
        if self.cabeza.heading() != UP:
            self.cabeza.setheading(DOWN)

    def left(self):
        if self.cabeza.heading() != RIGHT:
            self.cabeza.setheading(LEFT)

    def right(self):
        if self.cabeza.heading() != LEFT:
            self.cabeza.setheading(RIGHT)

    def reset(self):
        for seg in self.secciones:
            seg.goto(1000, 1000)
        self.secciones.clear()
        self.crear_snake()
        self.cabeza = self.secciones[0]
