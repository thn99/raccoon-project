import json


def sum_category(json_file):
    # Loading JSON file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    try:
        categories = []
        
        # Adding all categories to a list
        for product in json_db:
            if product['category'] not in categories:
                categories.append(product['category'])
        # Sorting list
        categories.sort()

        # Checking and calculating 'quantity * price' for every product, for each category
        for category in categories:
            category_value = 0
            for product in json_db:
                if product['category'] == category:
                    category_value += product['price'] * product['quantity']
            print(category, " - R$", category_value)
    except:
        print("Error! You must correct your file to run this function")


# Calling function
sum_category('./broken-database.json')