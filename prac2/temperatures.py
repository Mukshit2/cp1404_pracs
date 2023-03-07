MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_ToF():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def Farenheit_ToC():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_ToF()
    elif choice == "F":
        fahrenheit= float(input("fahrenheit: "))
        Farenheit_ToC()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")