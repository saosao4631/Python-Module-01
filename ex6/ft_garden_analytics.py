class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = 8.0
        self._stats = Plant.Statistics()

    @staticmethod
    def is_more_than_a_year(age: int) -> bool:
        if age <= 365:
            return False
        else:
            return True

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be nagative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height, 0)}")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be nagative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"age updated: {round(self._age, 0)}")

    def show(self) -> None:
        self._stats.count_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old"
        )

    def grow(self) -> None:
        self._stats.count_grow()
        self._height += self._growth_rate

    def age(self) -> None:
        self._stats.count_age()
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self._seeds = 0
        self._growth_rate = 30

    def age(self) -> None:
        self._stats.count_age()
        self._age += 20

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls = 0

        def count_produce_shade(self) -> None:
            self._produce_shade_calls += 1

        def show(self) -> None:
            super().show()
            print(f" {self._produce_shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.Statistics = Tree.Statistics()

    def produce_shade(self) -> None:
        self._stats.count_produce_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)} cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        self._growth_rate = 2.1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    age1 = 30
    age2 = 400
    print(
        f"Is {age1} days more than a year? -> "
        f"{Plant.is_more_than_a_year(age1)}"
    )
    print(
        f"Is {age2} days more than a year? -> "
        f"{Plant.is_more_than_a_year(age2)}"
    )
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)
    print(f"[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(f"[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    show_statistics(anonymous)
