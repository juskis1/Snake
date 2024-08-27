from turtle import Turtle

class Reset_Button(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.write("Play again", align="center", font=("Arial", 16, "underline"))
        self.penup()

    def button_click(self, screen, game):
        def click(x, y):
            if x > self.xcor() - 60 and x < self.xcor() + 60 and y > self.ycor() - 25 and y < self.ycor() + 25:
                screen.resetscreen()
                game()

        screen.onscreenclick(click)