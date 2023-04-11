MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_ToF(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit= float(input("fahrenheit: "))
            celsius = Farenheit_ToC(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")

def celsius_ToF(celsius):

    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def Farenheit_ToC(fahrenheit):

    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()