import json


def sum_values(json_file):
    json_db = json.load(open(json_file, 'r', encoding='utf8'))
    categories = []

    try:
        for product in json_db:
            if 'category' in product:
                if product['category'] not in categories:
                    categories.append(product['category'])

        for category in categories:
            sum_category = 0.0
            for product in json_db:
                if category == product['category']:
                    sum_category += product['price'] * product['quantity']
            print(category, "- total value: R$", sum_category)

    except:
        print('Error! Please execute all functions to correct the database')


