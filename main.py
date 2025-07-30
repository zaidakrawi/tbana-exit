from src.exits import load_exits

def main():
    exits = load_exits("data/data.json")
    print(f"Loaded {len(exits)} exits")
    print("First 3 exits:")
    for exit in exits[:3]:
        print(exit)



if __name__ == "__main__":
    main()