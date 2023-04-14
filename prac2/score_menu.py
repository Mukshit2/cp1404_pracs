def main():
    score = get_score()

    while True:
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ")

        if choice.upper() == "G":
            score = get_score()
        elif choice.upper() == "P":
            print_result(score)
        elif choice.upper() == "S":
            show_stars(score)
        elif choice.upper() == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def get_score():
    while True:
        try:
            score = int(input("Enter a score between 0 and 100: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    print("*" * score)


main()
