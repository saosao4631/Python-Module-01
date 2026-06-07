class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be nagative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height, 0)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be nagative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"age updated: {round(self._age, 0)} days")

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old"
            )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(-1)
    print()

    rose.set_height(-1.0)
    rose.set_age(-1)
    print()

    print("Current state:", end=" ")
    rose.show()
