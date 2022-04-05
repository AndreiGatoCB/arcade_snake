from turtle import Turtle

ALINEADO = "center"
FUENTE = ("Arial", 8, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.actualizacion_tablero()

    def actualizacion_tablero(self):
        self.write(f"Puntaje: {self.score} Puntaje máximo: {self.high_score}", align=ALINEADO, font=FUENTE)

    def sumar_puntaje(self):
        self.score += 1
        self.clear()
        self.actualizacion_tablero()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as puntaje_max:
            puntaje_max.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.actualizacion_tablero()
