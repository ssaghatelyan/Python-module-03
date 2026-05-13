import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        try:
            x = float(parts[0])
        except ValueError as ex:
            print(f"Error on parameter '{parts[0]}': {ex}")
            continue
        try:
            y = float(parts[1])
        except ValueError as ex:
            print(f"Error on parameter '{parts[1]}': {ex}")
            continue
        try:
            z = float(parts[2])
        except ValueError as ex:
            print(f"Error on parameter '{parts[2]}': {ex}")
            continue
        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tuple1 = get_player_pos()
    print(f"Got a first tuple: {tuple1}")
    print(f"It includes: X={tuple1[0]}, "
          f"Y={tuple1[1]}, Z={tuple1[2]}")
    x = tuple1[0]
    y = tuple1[1]
    z = tuple1[2]
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    tuple2 = get_player_pos()
    x1 = tuple2[0]
    y1 = tuple2[1]
    z1 = tuple2[2]
    distance1 = math.sqrt((x1-x)**2 + (y1-y)**2 + (z1-z)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance1, 4)}")


if __name__ == "__main__":
    main()
