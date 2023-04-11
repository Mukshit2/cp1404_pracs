import csv

# open the file and read data
with open('wimbledon.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    champions = {}
    countries = set()
    for row in reader:
        # extract champion and country from row
        champion, country = row[2], row[1]
        # add champion to dictionary and increment count
        champions[champion] = champions.get(champion, 0) + 1
        # add country to set
        countries.add(country)

# sort countries alphabetically and convert to list
countries = sorted(list(countries))

# display champions and their counts
print("Wimbledon Champions:")
for champion, count in sorted(champions.items()):
    print(f"{champion} {count}")

# display countries in alphabetical order
print(f"\nThese {len(countries)} countries have won Wimbledon:")
print(", ".join(countries))
