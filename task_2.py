import argparse
import turtle
import math

def draw_pythagoras_tree(t, length=100, depth=10):
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    left_branch_length = length * math.sqrt(2) / 2

    t.left(45)
    draw_pythagoras_tree(t, left_branch_length, depth - 1)
    t.right(90)
    draw_pythagoras_tree(t, left_branch_length, depth - 1)
    t.left(45)

    t.backward(length)


def main():
    parser = argparse.ArgumentParser(description='Pythagoras tree')
    parser.add_argument('-d', '--depth', required=True, type=int, help='Input tree depth')
    args = parser.parse_args()

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")

    length = 100

    draw_pythagoras_tree(t, length, args.depth)

    screen.exitonclick()

if __name__ == "__main__":
    main()
