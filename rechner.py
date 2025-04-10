import math

def main():
    history = []

    while True:
        print("\nTaschenrechner")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Potenzieren")
        print("6. Quadratwurzel")
        print("7. Prozentrechnung")
        print("8. Historie anzeigen")
        print("9. Beenden")

        choice = input("Wähle eine Option: ") #Auswahl eingabe

        if choice == "9":
            print("Programm wird beendet.")
            break

        if choice == "6":
            try:
                num = float(input("Zahl: "))
                result = math.sqrt(num)
                print(f"Ergebnis: {result}")
                history.append(f"{num} = {result}")
            except ValueError:
                print("Ungültige Eingabe.")
            continue

        if choice not in ["1","2","3","4","5","6","7","8"]:
            print("Sir, Y ARE YOU RUNNING!?")
            continue

        if choice == "8":
            print("\nHistorie:")
            for entry in history:
                print(entry)
            continue

        try:
            num1 = float(input("Erste Zahl: "))
            num2 = float(input("Zweite Zahl:"))
        except ValueError:
            print("Sir, Why are you mocking me..")
            continue

        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
        elif choice == "4":
            if num2 == 0:
                print("Nur Gott kann durch 0 teilen")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"
        elif choice == "5":
            result = num1 ** num2
            operation = f"{num1} ** {num2} = {result}"
        elif choice == "7":
            result = (num1 / 100) * num2
            operation = f"{num2}% von {num1} = {result}"

        print(f"Ergebnis: {result}")
        history.append(operation)
if __name__ == "__main__":
    main()























