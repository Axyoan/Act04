from math import pi


def get_square_area(side: float) -> float:
    return side * side


def get_circle_area(radius: float) -> float:
    return pi * radius * radius


def get_triangle_area(base: float, height: float) -> float:
    return (base * height) / 2.0


def func1():
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
            print('Area: ',
                  get_triangle_area(float(input("Base del tríangulo: ")), float(input("Altura del tríangulo: "))))


def func2():
    day = -1
    month = -1
    while month < 1 or month > 12:
        month = int(input("Ingrese mes de nacimiento (1-12)"))
    while day < 1 or day > 31:
        day = int(input("Ingrese día de nacimiento: "))

    print("Tu signo zodiacal es: ")
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Acuario")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Piscis")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Aries")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Tauro")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Géminis")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Cáncer")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Leo")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Virgo")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Libra")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Escorpio")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Sagitario    ")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Capricornio")


def main():
    op = "-1"
    while op != "0":
        print("1) Áreas: ")
        print("2) Signo zodiacal: ")
        print("3) Calcular e: ")
        print("0) Salir ")
        op = input()
        if op == "1":
            func1()
        elif op == "2":
            func2()


main()
