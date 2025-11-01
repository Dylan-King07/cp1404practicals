"""
CP1404 Practical 6 Guitars exercise
Estimated time: 10 minutes
Actual time: 10 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Function which collects and displays guitar information."""
    print("My Guitars!")

    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{guitars[-1]} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for index, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {index}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Maybe start by adding one!")


if __name__ == "__main__":
    main()
