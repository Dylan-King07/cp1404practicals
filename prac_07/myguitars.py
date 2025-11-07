"""
CP1404 prac_07 More Guitars! Exercise
Estimated time: 20 minutes
Actual time: 30 minutes
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read, display, add and save guitars to file."""
    # Load data from file
    guitars = load_guitars(FILENAME)

    # Display Data
    print("These are your guitars:")
    display_guitars(guitars)

    # Add new guitars
    print("Would you like to add a guitar?")
    guitars = create_guitars(guitars)

    # Display guitars sorted by year
    guitars.sort()
    print("Guitars sorted from oldest to newest:")
    display_guitars(guitars)

    # Save to CSV
    save_guitars_to_file(FILENAME, guitars)
    print(f"Guitars saved to {FILENAME}")


def load_guitars(filename):
    """Read guitars from file and return a list of them."""
    guitars = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            line = line.strip()
            name, year, cost = line.split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display list of guitars."""
    for index, guitar in enumerate(guitars, 1):
        vintage_guitars = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {index}: {guitar}{vintage_guitars}")


def create_guitars(guitars):
    """Create new guitar and add it to the list."""
    guitar_name = input("Name: ")
    while guitar_name:
        year_of_creation = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar = Guitar(guitar_name, year_of_creation, guitar_cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added.")
        guitar_name = input("Name: ")
    return guitars


def save_guitars_to_file(filename, guitars):
    """Write the guitars to the CSV file."""
    with open(filename, 'w', encoding='utf-8') as out_file:
        for guitar in guitars:
            print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
