from guitar import Guitar

print("My guitars!")
guitars = []
while True:
    name = input("Name: ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{str(guitar)} added.\n")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, start=1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i:<2}: {str(guitar):<30} worth ${guitar.cost:>12,.2f}{vintage_string}")

