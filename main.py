from src.exits import load_exits
from src.geocoding import geocode
from src.finder import closest_exit

def main():
    address = input("Where do you want to go?: ")
    user_coords = geocode(address)

    exits = load_exits("data/data.json")
    closest = closest_exit(user_coords, exits)

    print(closest)



if __name__ == "__main__":
    main()