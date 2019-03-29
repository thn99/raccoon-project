import json


def right_quantity(json_file):
    # Loading JSON file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Adding quantity = 0 to products with no quantity
    for product in json_db:
        if 'quantity' not in product:
            product['quantity'] = 0

    write_json = open(json_file, 'w', encoding='utf8')
    # Encoding (in order to prevent having problems with wrong characters) and transforming python dict to JSON
    right_file = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')
    # Overwriting corrections to file
    write_json.write(right_file)


# Calling function
right_quantity('./broken-database.json')