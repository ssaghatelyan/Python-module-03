import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        x = 1
        while x < len(sys.argv):
            print(f"Argument {x}: {sys.argv[x]}")
            x += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
