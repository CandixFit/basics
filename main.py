"""def ausgabe_zahlen():
    a = 0
    while (a <= 10):
        print(a)
        a = a + 1
ausgabe_zahlen()"""

"""summe = 0
while True:
    zahl = input("Bitte eine Zahl eingeben (0 zum Beenden): ")
    if zahl == "0":
        break
    summe += int(zahl)
print("Die Summe ist:", summe)"""

"""passwort = "geheim"
while True:
    eingabe = input("Bitte Passwort eingeben: ")
    if eingabe == passwort:
        print("Zugang gewährt!")
        break
    print("Falsches Passwort, versuche es erneut.")"""

"""for i in range (1, 11):
    print(i)"""

"""for i in range (2, 21, 2):
    print(i)"""

"""zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range (0, len(zahlen), 5):
    print(zahlen[i])"""

"""for i in range(5):
    for j in range(5):
        print("*", end="")
    print()"""

"""for i in range (10, 0, -1):
    print(i)"""

"""namen = ["Anna", "Max", "Tom", "Lisa"]
namen.append("Marie")
namen.remove("Tom")
print("Länge der Liste:", len(namen))"""

"""zahlen = ["5", "3", "8", "1", "2"]
zahlen.sort()
print("Aufsteigend:", zahlen)
zahlen.sort(reverse=True)
print("Absteigend:", zahlen)
zahlen.reverse()
print("Umgekehrt", zahlen)"""

"""liste = [1, 2, 3, 4, 5]
liste.append(6)
liste.insert(0, 0)
print("Anzahl der 3er:", liste.count(3))"""

"""werte = [10, 20, 30, 40, 50]
for wert in werte:
    print(wert)"""

"""liste = [1, 2, 3, 4, 5]
summe = 0
for nummer in liste:
    summe += nummer
print("Summe:", summe)"""

"""test = "Hallo"
for buchstabe in test:
    print(buchstabe)"""

"""liste = [21, 5, 312, 51, 5]
for zahl in liste:
    if zahl > 10:
        print(zahl)"""

"""liste = [10, 20, 30, 40]
for i in range(len(liste)):
    print("Index:", i, "Wert:", liste[i])"""

"""werte = [10, 20, 30, 40, 50]
for index, wert in enumerate(werte):
    print("Index", index, "Wert:", wert)"""

"""anzahl = 6
i = 0
summe = 0
temperaturen = [] #anlegen einer liste

while i < anzahl:
    print("Geben sie die {0}. Temperatur in °C ein: ".format(i+1))
    eingabe = float(input())
    temperaturen.append(eingabe) # element am ende der liste hinzufügen
    summe = summe + temperaturen[i] #auf listenelement zugreifen
    i = i + 1
durchschnitt = summe / anzahl
print("Der Temperaturendurchschnitt beträgt: ",durchschnitt)"""

"""import random
anzahl = 6
i = 0
summe = 0
temperaturen = [] #anlegen einer liste

while i < anzahl:
    print("Geben sie die {0}. Temperatur in °C ein: ".format(i+1))
    eingabe = random.gauss(0, 10)
    temperaturen.append(eingabe) # element am ende der liste hinzufügen
    summe = summe + temperaturen[i] #auf listenelement zugreifen
    i = i + 1
    print(temperaturen)
durchschnitt = summe / anzahl
print("Der Temperaturendurchschnitt beträgt: ",durchschnitt)""" #selbe element mit zufallsgenerator

"""for erste in range(1):
    for sieben in range(7):
        print("*", end="")
    print()

for zweite in range(1):
    for fuenf in range(5):
        print("*", end="")
    print()

for dritte in range(1):
    for drei in range(3):
        print("*", end="")
    print()

for vierte in range(1):
    for vier in range(1):
        print("*", end="")
    print()"""    #for schleife um bestimmtes sternenbild anzugeben

"""zahl = int(input("Zahl eingebne: "))
fakultaet = 1
for i in range(1, zahl + 1):
    fakultaet *= i
print(f"Die Fakultät von {zahl} ist {fakultaet}")""" #fakultaet berechnen

"""import json
from datetime import datetime
speicheroption = []
def show_menu():
    print("\nBitte Wählne")
    print("1. Aufgabe hinzufügen")
    print("2. alle Aufgaben anzeigen")
    print("3. Aufgabe bearbeiten")
    print("4. Aufgabe löschen")
    print("5. Beenden")
show_menu()"""


"""def to_camel_case(text):
    if not text:
        return text

    words = text.replace('-',' ').replace('_', ' ').split()

    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

print(to_camel_case("the-stealth-warrior"))  # Output: "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior"))  # Output: "TheStealthWarrior"
print(to_camel_case("The_Stealth-Warrior"))  # Output: "TheStealthWarrior""""

"""handle = open("text.txt", "r")
inhalt = handle.read() #lesen mit dieser funktion die datei
print(inhalt)
handle.close()"""
"""file = open("text.txt", "r")
inhalt = file.read()
print(inhalt)
file.close()"""

"""with open("text.txt", "r") as file:
    inhalt = file.read()
    file.readline(6) #byte begrenzzen
    file.readlines()
    print(inhalt)
    file.close()"""

#schreiben von textdateien
"""text = "die regierung hat mir in die hosen gekackt11!11!"

handle = open("text.txt", "w")
geschrieben = handle.write(text)
handle.close()
print(text)"""
