import csv


def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def process_wimbledon_data(data):
    champions = {}
    countries = set()

    for row in data[1:]:  # Skip header
        champion = row[2]
        country = row[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)

    return champions, countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items(), key=lambda item: item[0]):
        print(f"{champion} {wins}")


def display_countries(countries):
    sorted_countries = sorted(countries)
    print("\nThese", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champions, countries = process_wimbledon_data(data)
    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()
