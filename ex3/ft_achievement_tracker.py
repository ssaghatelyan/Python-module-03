import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"
    ]
    count = random.randint(4, 8)
    return set(random.sample(achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    all_achievements = set.union(Alice, Bob, Charlie, Dylan)

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print(f"\nAll distinct achievements: {all_achievements}")
    print(f"\nCommon achievements: "
          f"{set.intersection(Alice, Bob, Charlie, Dylan)}")

    print(f"\nOnly Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")

    print(f"\nAlice is missing: {all_achievements.difference(Alice)}")
    print(f"Bob is missing: {all_achievements.difference(Bob)}")
    print(f"Charlie is missing: {all_achievements.difference(Charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(Dylan)}")


if __name__ == "__main__":
    main()
