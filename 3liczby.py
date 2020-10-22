#!/usr/bin/env python3
# -*- coding: utf-8 -*_

op = "t"
while op == "t":

    data = input("Podaj trzy liczby oddzielone spacjami: ")

    if data.find(",") == 1:
        try:
            a, b, c = data.split(",")
        except ValueError:
            print("Za mała liczba argumentów")
            break
    else:
        try:
            a, b, c = data.split(" ")
        except ValueError:
            print("Za mała liczba argumentów")
            break

    print("Wprowadzono liczby: ", a, b, c)
    print("\nNajmniejsza:")

    a = int(a)
    b = int(b)
    c = int(c)

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = b
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    op = input("Jeszcze raz (t/n)?")

print("Koniec")
