from pprint import pprint


def read_recipes_from_file(filename):

    temp_cookbook_dict = dict()
    next_line_is_dish_name = True
    next_line_is_ingredient_count = False
    temp_ingredient_count = 0


    with open(filename, encoding='utf8') as f:
        for line in f:
            if next_line_is_dish_name:
                dish_name = line.strip()
                temp_cookbook_dict.update({dish_name: list()})
                next_line_is_dish_name = False
                next_line_is_ingredient_count = True

            elif next_line_is_ingredient_count:
                temp_ingredient_count = int(line.strip())
                next_line_is_ingredient_count = False

            elif temp_ingredient_count > 0:
                line = line.strip()
                temp_ingredient = line.split(' | ')
                temp_cookbook_dict[dish_name].append({'ingredient_name': temp_ingredient[0], 'quantity': temp_ingredient[1], 'measure': temp_ingredient[2]})
                temp_ingredient_count -= 1

            elif temp_ingredient_count == 0:
                next_line_is_dish_name = True

    return temp_cookbook_dict


def get_shop_list_by_dishes(dishes, person_count, cookbook):
    temp_ingredients = dict()
    for dish in dishes:
        for ingredient in cookbook[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            if temp_ingredients.get(ingredient_name, False):
                quantity = temp_ingredients[ingredient_name]['quantity'] + int(ingredient['quantity'])*person_count
            else:
                quantity = int(ingredient['quantity'])*person_count
            temp_ingredients.update({ingredient_name: {'measure': measure, 'quantity': quantity}})

    return temp_ingredients


pprint(get_shop_list_by_dishes(['Фо-Бо', 'Фахитос', 'Омлет'], 22, read_recipes_from_file('recipes.txt')))

