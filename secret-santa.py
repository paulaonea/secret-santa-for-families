
# Rules:
# 1- no family member can be paired with someone from the same family
# 2 - children are paired between themselves
# 3 - adults are paired between themselves

import random


def add_families():
    while True:
        print('Add more families? (y, n): ')
        if input() == 'y':
            add_family()
        else:
            break


def add_family():
    family = input("Enter family name: ")
    children = input(f"Enter the name of the family {family}'s children, separated by coma: ")
    adults = input(f"Enter the name of the family {family}'s adults, separated by coma: ")
    families[family] = {
        'children': [child.strip(' ') for child in children.split(',')],
        'adults': [adult.strip(' ') for adult in adults.split(',')]
    }


def set_options(dictionary):
    for family in dictionary.keys():
        children_options = []
        adults_options = []
        for otherFamily in dictionary.keys():
            if family != otherFamily:
                for child in dictionary[otherFamily]['children']:
                    children_options.append(child)
                for adult in dictionary[otherFamily]['adults']:
                    adults_options.append(adult)
        options[family] = {
            'children': children_options,
            'adults': adults_options
        }


def get_pairs():
    allChildren = [child for family in families.keys() for child in families[family]['children']]
    allAdults = [adult for family in families.keys() for adult in families[family]['adults']]
    for family in families.keys():
        for child in families[family]['children']:
            choice = set(allChildren).intersection(options[family]['children'])
            pair = random.choice(tuple(choice))
            pairs.append((child, pair))
            allChildren.remove(pair)
        for adult in families[family]['adults']:
            choice = set(allAdults).intersection(options[family]['adults'])
            pair = random.choice(tuple(choice))
            pairs.append((adult, pair))
            allAdults.remove(pair)


families = {}
add_families()

options = {}
set_options(families)

print(options)

pairs = []
get_pairs()

print(pairs)
