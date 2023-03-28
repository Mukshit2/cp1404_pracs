COLOUR_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "Beige": "#f5f5dc",
    "CadetBlue": "#5f9ea0",
    "CornflowerBlue": "#6495ed",
    "Crimson": "#dc143c",
    "DarkBlue": "#00008b",
    "DarkGreen": "#006400",
    "DarkSlateBlue": "#483d8b",
    "DarkViolet": "#9400d3",
    "Goldenrod": "#daa520"
}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").title()