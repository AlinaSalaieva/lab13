class ROCK:
    def __init__(self, name, height, continent, country):
        self.name = name
        self.height = height
        self.continent = continent
        self.country = country

    def change_height(self, new_height):
        self.height = new_height

    def __str__(self):
        return f"{self.name} ({self.height}м, {self.continent}, {self.country})"

rocks = []
rocks.append(ROCK("Еверест", 8848, "Азія", "Непал"))
rocks.append(ROCK("Кіліманджаро", 5895, "Африка", "Танзанія"))
rocks.append(ROCK("Монблан", 4810, "Європа", "Франція"))

def remove_rock_by_name(rocks, name):
    rocks = [rock for rock in rocks if rock.name != name]
    return rocks

rocks.sort(key=lambda rock: rock.name)

print("Всі гори:")
for rock in rocks:
    print(rock)

print("\nПісля видалення Кіліманджаро:")
rocks = remove_rock_by_name(rocks, "Кіліманджаро")
for rock in rocks:
    print(rock)
