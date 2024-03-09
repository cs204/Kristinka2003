def main():
    fruit = input("Фрукт: ")
    calories(fruit)

def calories(fruit):
    calories_fruit = {
        "Apple": 130,
        "Avocado": 50,
        "Lime": 20
    }

    if fruit in calories_fruit:
        calories = calories_fruit[fruit]
        print(f"Калории: {calories}")

if __name__ == "__main__":
    main()
