def main():
    questions = [
        ("Hauptstadt der baguettes und croissants?", ["Paris","London","Berlin","Madrid"], "Paris"),
        ("Wie viele Kontinente gibt es auf der Erde?", ["5","6","7","8"], "7"),
        ("Wer hat die Kekse aus der Dose geklaut?", ["Die Mama", "Der Papa", "Das Krümmelmonster"], "Das Krümmelmonster"),
        ("Welches Element hat das Symbol 'O'?", ["Gold", "Osmium", "Oxygen", "Zinn"], "Oxygen"),
        ("Wie viele Tage hat ein Schaltjahr?", ["365", "366", "364", "360"], "366"),
        ("Welche Programmiersprache lernen wir hier?", ["Python", "Java", "C++", "Ruby"], "Python"),
        ("Was ist die Wurzel von 81?", ["7", "8", "9", "10"], "9"),
        ("Wie viele Planeten hat unser Sonnensystem?", ["7", "8", "9", "10"], "8"),
        ("Wie heißt der größte Ozean?", ["Atlantik", "Indischer Ozean", "Pazifik", "Arktis"], "Pazifik"),
        ("Welcher Planet ist der Sonne am nächsten?", ["Venus", "Merkur", "Mars", "Jupiter"], "Merkur"),


    ]
    score = 0
    for idx, (question, options, answer) in enumerate(questions, 1):
        print(f"\nFrage {idx}: {question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Deine Antwort: "))
            if options[choice - 1] == answer:
                print("Richtig!")
                score += 1
            else:
                print(f"Falsch! Die richtige Antwort war: {answer}")
        except(ValueError,IndexError):
            print(f"Üngültige Eingabe. Richtige Antwort: {answer}")

    print(f"\nDein Punktestand: {score} von {len(questions)}")
if __name__ == "__main__":
    main()
