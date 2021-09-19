#!/usr/bin/env python3


add_food = {"CottonCandyBlue": 71, "Chocolate": 1}
all_food = {'Meat': 0, 'Milk': 0, 'Strawberry': 0,
            'CottonCandyBlue': 0, 'Honey': 0}

add_food.update(all_food)
print(add_food)
# {'CottonCandyBlue': 0, 'Chocolate': 1, 'Meat': 0, 'Milk': 0, 'Strawberry': 0, 'Honey': 0}


add_food2 = {"CottonCandyBlue": 71, "Chocolate": 1}
all_food2 = {'Meat': 0, 'Milk': 0, 'Strawberry': 0,
             'CottonCandyBlue': 0, 'Honey': 0}


all_food2.update(add_food2)
print(all_food2)
# {'Meat': 0, 'Milk': 0, 'Strawberry': 0, 'CottonCandyBlue': 71, 'Honey': 0, 'Chocolate': 1}
