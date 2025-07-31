from src.exits import load_exits
from src.geocoding import geocode
from src.finder import closest_exit

def main():
    address = input("Where do you want to go?: ")
    user_coords = geocode(address)

    exits = load_exits("data/data.json")
    closest = closest_exit(user_coords, exits)

    print(f"\nStation: {closest['station']}")
    print(f"Exit name: {closest['exit_name']}")
    print(f"Distance: {closest['distance']:.1f} meters")
    print(f"Direction: {closest['direction']}")



if __name__ == "__main__":
    main()