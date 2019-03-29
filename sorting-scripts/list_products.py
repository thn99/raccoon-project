import json


def list_products(json_file):
    # Loading JSON file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    categories = []
    id_list = []

    # Add all IDs and categories to the previously created lists
    for product in json_db:
        if product['category'] not in categories:
            categories.append(product['category'])
        if product['id'] not in id_list:
            id_list.append(product['id'])
    
    # Sorting lists
    categories.sort()
    id_list.sort()
    
    print("-"*50)
    print("Sorting by: CATEGORY")
    print("-"*50)

    # Prints products sorted by CATEGORY
    for category in categories:
        for product in json_db:
            if product['category'] == category:
                print(category, '-', product['name'])
    print("-"*50)
    print("Sorting by: ID")
    print("-"*50)

    # Prints products sorted by ID
    for number in id_list:
        for product in json_db:
            if product['id'] == number:
                print(number, '-', product['name'])


# Calling function
list_products('./broken-database.json')