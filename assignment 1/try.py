VISITED_CHAR = 'v'
UNVISITED_CHAR = 'n'
FILENAME = 'places.csv'


def load_places():
    places = []
    with open('places.csv', 'r') as file:
        for line in file:
            place = line.strip().split(',')
            places.append(place)
    return places


def display_menu():
    print('Menu:')
    print('L - List places')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')


def get_menu_choice():
    choice = input('>>> ').upper()
    while choice not in ['L', 'A', 'M', 'Q']:
        print('Invalid choice')
        choice = input('>>> ').upper()
    return choice


def display_places(places):
    """
    Display a list of places with their indexes, names, countries, and priority levels.
    """
    if not places:
        print("No places to display.")
    else:
        print("Your places:")
        for i, place in enumerate(sorted(places, key=lambda x: (x[3], -int(x[2])), start=1)):
            print(f"{i}. {place[1]} in {place[0]} {place[2]}")
        print(f"{len(places)} places. You still want to visit")




def add_place(places):
    """Add a new place to the list."""
    name = input("Name: ")
    while True:
        try:
            country = input("Country: ")
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Please enter a valid integer for priority.")

    new_place = [name, country, priority, "n"]
    places.append(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_place_visited(places):
    """Mark a place as visited."""
    unvisited_places = get_unvisited_places(places)
    if not unvisited_places:
        print("No unvisited places.")
        return

    print("Places you can visit:")
    display_places(unvisited_places)

    while True:
        try:
            choice = int(
                input("Enter the number of a place to mark as visited: "))
            if choice not in range(1, len(unvisited_places) + 1):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Enter a number between 1 and",
                  len(unvisited_places))

    index = places.index(unvisited_places[choice - 1])
    name, country, priority, status = places[index]
    places[index] = [name, country, priority, "v"]
    print(f"{name} in {country} marked as visited.")


def save_places(places):
    """Save places to the CSV file."""
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(places)


def main():
    """Travel Tracker program."""
    print("Travel Tracker 1.0 - by Your Name")

    places = load_places()
    print(f"{len(places)} places loaded from {FILENAME}")
    display_menu()
    while True:
        choice = get_menu_choice()
        if choice == "L":
            display_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_place_visited(places)
        elif choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break


main()
