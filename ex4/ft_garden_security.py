class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self.get_height(), 0)}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"age updated: {round(self.get_age(), 0)} days")

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        current_height = self.get_height()
        self.set_height(current_height + 0.8)

    def age(self) -> None:
        current_age = self.get_age()
        self.set_age(current_age + 1)

    def show(self) -> None:
        print(f"{self._name}:", end=" ")
        print(f"{round(self.get_height(), 1)}cm,", end=" ")
        print(f"{self.get_age()} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print()

    rose.set_height(-1.0)
    rose.set_age(-1)
    print()

    print("Current state:", end=" ")
    rose.show()
