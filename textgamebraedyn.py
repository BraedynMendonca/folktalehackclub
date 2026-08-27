room = "start"
coins = 0
math_done = False
word_done = False
game_running = True

print("Welcome to Escape the Lab!")

while game_running:

    if room == "start":
        print("\nYou are trapped in a strange lab.")
        print("A locked exit needs 2 coins.")
        print("1. Try the exit")
        print("2. Enter the main room")

        choice = input("Choose 1 or 2: ")

        if choice == "1":
            room = "exit"
        elif choice == "2":
            room = "main"
        else:
            print("Invalid choice.")

    elif room == "main":
        print("\nYou are in the main room.")
        print("1. Math Room")
        print("2. Word Room")
        print("3. Go back")

        choice = input("Choose 1-3: ")

        if choice == "1":
            room = "math"
        elif choice == "2":
            room = "word"
        elif choice == "3":
            room = "start"
        else:
            print("Invalid choice.")

    elif room == "math":
        if math_done:
            print("\nYou already completed this room.")
            room = "main"
        else:
            print("\nSolve: 6 + 3 * 2")
            answer = input("Answer: ")

            if answer == "12":
                print("Correct! You earned a coin.")
                coins += 1
                math_done = True
                room = "main"
            else:
                print("Incorrect. Try again later.")
                room = "main"

    elif room == "word":
        if word_done:
            print("\nYou already completed this room.")
            room = "main"
        else:
            print("\nUnscramble this word: NPYTOH")
            answer = input("Answer: ").lower()

            if answer == "python":
                print("Correct! You earned a coin.")
                coins += 1
                word_done = True
                room = "main"
            else:
                print("Incorrect. Try again later.")
                room = "main"

    elif room == "exit":
        if coins >= 2:
            print("\nYou insert both coins.")
            print("The door opens. You escaped!")
            game_running = False
        else:
            print("\nYou need 2 coins, but you only have", coins)
            room = "start"

print("Thanks for playing!")