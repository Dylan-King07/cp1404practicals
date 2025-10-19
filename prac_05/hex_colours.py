# Dictionary of 10 colour names
COLOUR_HEX_CODE = {
    "aliceblue": "#f0f8ff",
    "amber": "#ffbf00",
    "alizarincrimson": "#e32636",
    "armygreen": "#4b5320",
    "barnred": "#7c0a02",
    "bitterlime": "#bfff00",
    "britishracinggreen": "#004225",
    "byzantine": "#bd33a4",
    "byzantium": "#702963",
    "celticblue": "#246bce"
}

# Input valid colour name and print HEX code
input_colour_name = input("Enter colour name: ").lower()
while input_colour_name != "":
    try:
        print(f"{input_colour_name} has hex code {COLOUR_HEX_CODE[input_colour_name]}")
    except KeyError:
        print("Invalid colour name")
    input_colour_name = input("Enter colour name: ").lower()
