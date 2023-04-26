"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car

def main():
    """Demo test code to show how to use car class."""
    # create a new car object called "limo" with 100 units of fuel
    limo = Car(name="Limo", fuel=100)

    # add 20 more units of fuel to limo using the add method
    limo.add_fuel(20)

    # print the amount of fuel in limo
    print(f"{limo.name} has {limo.fuel} units of fuel.")

    # attempt to drive limo 115 km using the drive method
    driven_distance = limo.drive(115)

    # display how far limo was actually driven
    print(f"{limo.name} drove {driven_distance} km.")

    # display limo's current state using __str__ method
    print(limo)


main()
