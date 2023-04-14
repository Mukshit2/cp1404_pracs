'''
Name: Mukshit 
student id - jc955870
GITHUB URL - https://github.com/Mukshit2/cp1404/tree/main/assignment%201

'''

import csv
import random

# Constants
FILENAME = "places.csv"
HEADER = ["Name", "Country", "Priority", "Visited"]
UNVISITED_MARK = "*"

# Main program


def main():
    places = load_places()
    print("Travel Tracker 1.0 - by Mukshit")
    print(f"{len(places)} places loaded from {FILENAME}")

    max_name_len = max(len(place[0]) for place in places)
    max_country_len = max(len(place[1]) for place in places)

    while True:
        sorted(
        places, key=lambda place: (place[3], -int(place[2])))
        print("Menu:")
        print("L - List places")
        print("A - Add new place") 
        print("M - Mark a place as visited")
        print("R - Recommend a place to visit")
        print("Q - Quit\n")
        choice = input(">>> ").upper()
        if choice == "L":
            display_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places, max_name_len, max_country_len)
        elif choice == "R":
            recommend_place(places)
        elif choice == "Q":
            save_places(places)
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice!")


# Functions
def load_places():
    """
    Load places from a CSV file and return a list of lists
    """
    places = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            places.append(row)
    return places


def save_places(places):
    """
    Save places to a CSV file
    """
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        for place in places:
            writer.writerow(place)


def display_places(places):
    """
    Display a neatly formatted list of all places with details and number of unvisited places
    """
    places_left = sum(place[3] == "n" for place in places)
    max_name_len = max(len(place[0]) for place in places)
    max_country_len = max(len(place[1]) for place in places)
    print(
        f"{''*(max_name_len-4)}{''*(max_country_len-7)}")
    print(""*(max_name_len+max_country_len+20))
    #sorted_places = sorted(
     #   places, key=lambda place: (place[3], -int(place[2])))
    for i,place in enumerate (places,1):
        visited_mark = UNVISITED_MARK if place[3] == "n" else " "
        print(f"{visited_mark}{i}. {place[0]:{max_name_len}} in {place[1]:{max_country_len}}"
              f"{place[2]:>8}")
    if places_left == 0:
        print(f"{len(places)}. No places left to visit. Why not add a new place?")
    else:
        print(
            f"\n{len(places)} places. You still want to visit {places_left} places.\n")


def get_valid_input(prompt):
    """
    Get a valid input from the user
    """
    variable = input(prompt)
    while variable == "":
        print("input cannot be blank .")
        variable = input(prompt)
    return variable


def add_place(places):
    """
    Prompt the user to add a new place to the list
    """
    name = get_valid_input("Name: ")
    country = get_valid_input("Country: ")
    priority = get_valid_input("Priority: ")
    visited = "n"
    places.append([name, country, priority, visited])
    print(f"\n{name} in {country} (priority {priority}) added to Travel Tracker.\n")


def mark_visited(places, max_name_len, max_country_len):
    unvisited_places = [place for place in places if place[3] == "n"]
    if not unvisited_places:
        print("No unvisited places")
        return

    # print the list of places
    display_places(places)

    # get user input for place to mark as visited
    while True:
        try:
            choice = int(
                input("Enter the number of a place to mark as visited: "))
            if choice < 1 or choice > len(places):
                raise ValueError
            elif places[choice - 1][3] == "y":
                print("That place has already been visited.")
            else:
                places[choice - 1][3] = "y"
                print(
                    f"{places[choice - 1][0]} in {places[choice - 1][1]} marked as visited.")
                break
        except ValueError:
            print(f"Please enter a number between 1 and {len(places)}")


def recommend_place(places):
    """
    Recommend a random unvisited place
    """
    unvisited_places = [place for place in places if place[3] == "n"]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(
            f"\nNot sure where to visit next? \nHow about... {place[0]} in {place[1]}?\n")
    else:
        print("\nNo places left to visit!\n")


main()
