# src/app.py
import argparse
from src.rules import study_suggestion

def main():
    parser = argparse.ArgumentParser(
        prog="app",
        description="Hello CLI - Capstone starter"
    )
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument("--time", choices=["short","medium","long"], help="Time available")
    parser.add_argument("--energy", choices=["low","high"], help="Energy level")
    args = parser.parse_args()

    print(f"Hello, {args.name}! This is our Capstone starter.")

    if args.time or args.energy:
        t = args.time or ""
        e = args.energy or ""
        print(study_suggestion(t, e))

if __name__ == "__main__":
    main()
