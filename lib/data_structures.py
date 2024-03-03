import ipdb
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    spicy_food = [food.get("name") for food in spicy_foods]
    return spicy_food


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spiciest for spiciest in spicy_foods if spiciest.get("heat_level") > 5]
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    return [print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}") for food in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}")


def get_average_heat_level(spicy_foods):
    heat_level = 0
    for food in spicy_foods:
        heat_level += food.get('heat_level')
    return heat_level / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods


print(create_spicy_food(spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))
