import csv
filename = wimbledon.csv
def read_file(filename):
    champions = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            champions.append(row)
    return champions

def get_champions(champions):
    champ_dict = {}
    for champ in champions:
        name = champ[0]
        count = int(champ[1])
        champ_dict[name] = count
    return champ_dict

def get_countries(champions):
    countries = set()
    for champ in champions:
        country = champ[2]
        countries.add(country)
    countries_list = sorted(list(countries))
    countries_string = ', '.join(countries_list)
    return countries_string

def main():
    filename = 'wimbledon.csv'
    champions = read_file(filename)
    champ_dict = get_champions(champions)
    countries_string = get_countries(champions)
    print("Wimbledon Champions:")
    for name, count in champ_dict.items():
        print(f"{name} {count}")
    print(f"\nThese {len(countries_string.split(', '))} countries have won Wimbledon:")
    print(countries_string)

if __name__ == '__main__':
    main()
