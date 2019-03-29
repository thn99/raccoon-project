import json


def right_prices(json_file):
    # Loading JSON file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Converting all prices to float, so it corrects all errors
    for product in json_db:
        if 'price' in product:
            old_price = product['price']
            new_price = float(old_price)
            product['price'] = new_price
    
    # Opening file to write
    write_json = open(json_file, 'w', encoding='utf8')
    # Encoding (in order to prevent having problems with wrong characters) and transforming python dict to JSON
    right_file = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')
    write_json.write(right_file)


# Calling function
right_prices('./broken-database.json')