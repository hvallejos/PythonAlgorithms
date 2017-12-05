# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    rect = turtle.Turtle()
    make_square(rect)
    turtle.mainloop()

def make_square(rect):
    length = int(raw_input('Ingrese tamaño: '))
    for i in range(4):
        make_line_and_turn(rect, length)

def make_line_and_turn(rect, length):
    rect.forward(length)
    rect.left(90)

if __name__ == '__main__':
    main()