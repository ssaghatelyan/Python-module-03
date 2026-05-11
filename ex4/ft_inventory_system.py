import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    if len(sys.argv) < 2:
        print("Got inventory: {}")
        print("Item list: []")
        print("Total quantity of the 0 items: 0")
        return

    args = sys.argv[1:]

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty = arg.split(":", 1)

        if item == "" or qty == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    sumV = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {sumV}")

    for item in inventory:
        percent = round((inventory[item] / sumV) * 100, 1)
        print(f"Item {item} represents {percent}%")

    items = list(inventory.keys())
    most = least = items[0]

    for item in inventory:
        if most is None or inventory[item] > inventory[most]:
            most = item
        if least is None or inventory[item] < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({'magic_item': 1})

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
