"""
Wimbledon
Estimated time: 1 hour
Actual time: 1 hour
"""

FILENAME = "wimbledon.csv"


def main():
    """
    Main function
    """
    records = load_champion_data(FILENAME)
    champion_win_counts, champion_countries = process_champion_data(records)
    print_results(champion_win_counts, champion_countries)


def load_champion_data(filename):
    """Read file and return list of champions and their countries"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            split_results_into_parts = line.strip().split(",")
            champion_name = split_results_into_parts[2]
            champion_country = split_results_into_parts[1]
            records.append([champion_name, champion_country])
    return records


def process_champion_data(records):
    """Create dictionary of champion win counts and countries"""
    champion_win_counts = {}
    champion_countries = set()

    for champion_name, country in records:
        champion_win_counts[champion_name] = champion_win_counts.get(champion_name, 0) + 1
        champion_countries.add(country)

    return champion_win_counts, champion_countries


def print_results(champion_win_counts, champion_countries):
    """Print champion data with correct formatting"""
    print("Wimbledon Champions: ")
    for champion_name, wins in champion_win_counts.items():
        print(f"{champion_name} {wins}")
    print()
    sort_countries = sorted(champion_countries)
    print(f"These {len(sort_countries)} countries have won Wimbledon:")
    print(", ".join(sort_countries))


main()
