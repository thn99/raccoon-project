import json


def right_prices(json_file):

    # Loading json file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Converting all prices into FLOAT type, so no price stays wrong.
    for product in json_db:
        if 'price' in product:
            old_price = product['price']
            new_price = float(old_price)
            product['price'] = new_price

    # Converting dict to JSON again, encoding with 'utf8' so the file remains intact
    right_json = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')

    # Overwrite json file with the right prices
    write_json = open(json_file, 'w', encoding='utf8')
    write_json.write(right_json)

