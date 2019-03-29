import json


def sort_products(json_file):
    json_db = json.load(open(json_file, 'r', encoding='utf8'))
    categories = []
    product_id = []

    # Creating content on lists for later sorting
    for product in json_db:
        if 'category' in product:
            if product['category'] not in categories:
                categories.append(product['category'])
        if 'id' in product:
            if product['id'] not in product_id:
                product_id.append(product['id'])

    # Sorting categories by alphabetical order && id by ascending order
    categories.sort()
    product_id.sort()

    # Print by category, sorted by the previously created list
    print("-" * 30 + "\nListing products by: Category\n" + "-" * 30)
    for category in categories:
        for product in json_db:
            if product['category'] == category:
                print(product['category'], "-", product['name'])

    # Print by id, sorted by the previously created list
    print("-"*30 + "\nListing products by: ID\n" + "-"*30)
    for id_number in product_id:
        for product in json_db:
            if product['id'] == id_number:
                print(product['id'], "-", product['name'])

sort_products('./broken-database.json')