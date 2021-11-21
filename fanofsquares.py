import turtle


def main():
    print("Please enter number of squares: ")
    n = int(input())
    turtle_fan_of_squares(n, 100)
    turtle.done()


def turtle_square(side_len):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)


def turtle_fan_of_squares(num_of_squares, side_len):
    for count in range(num_of_squares):
        turtle.speed(3000)
        turtle.hideturtle()
        turtle_square(side_len)
        turtle.left(360 / num_of_squares)


main()
