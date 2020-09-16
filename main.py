from math import pi


def get_square_area(side: float) -> float:
    return side * side


def get_circle_area(radius: float) -> float:
    return pi * radius * radius


def get_triangle_area(base: float, height: float) -> float:
    return (base * height) / 2.0


op = 1
while op != "0":
    print("1)Cuadrado: ")
    print("2)Círculo: ")
    print("3)Tríangulo: ")
    print("0)Salir: ")
    op = input()
    if op == '1':
        print('Area: ', get_square_area(float(input("Lado del cuadrado: "))))
    elif op == '2':
        print('Area: ', get_circle_area(float(input("Radio del círculo: "))))
    elif op == '3':
        print('Area: ', get_triangle_area(float(input("Base del tríangulo: ")), float(input("Altura del tríangulo: "))))
