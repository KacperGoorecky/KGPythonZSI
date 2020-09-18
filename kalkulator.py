row = input("Jaki rodzaj działania wykonasz? (1.dodawanie/2.odejmowanie/3.mnożenie/4.dzielenie/5.reszta): ")

if row == "1" or row == "dodawanie" or row == "1.dodawanie" or row == "+":
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")
    print(float(x) + float(y))

if row == "2" or row == "odejmowanie" or row == "2.odejmowanie" or row == "-":
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")
    print(float(x) - float(y))

if row == "3" or row == "mnożenie" or row == "3.mnożenie" or row == "*":
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")
    print(float(x) * float(y))

if row == "4" or row == "dzielenie" or row == "4.dzielenie" or row == "/":
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")
    print(float(x) / float(y))

if row == "5" or row == "reszta" or row == "5.reszta" or row == "%":
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")
    print(float(x) % float(y))