from food import Food
from replay import Reset_Button
from snake import Snake
from scoreboard import Scoreboard
from turtle import Screen
import time


icon = Screen()._root
icon.iconbitmap("snake.ico")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


def game():

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True

    while game_on:
        screen.update()
        # Snake speed
        time.sleep(0.1)

        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            scoreboard.game_over()
            replay = Reset_Button()
            replay.button_click(screen, game)

        # Collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()
                replay = Reset_Button()
                replay.button_click(screen, game)

    screen.mainloop()

game()