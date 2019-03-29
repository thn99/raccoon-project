import json


def right_quantity(json_file):
    # Loading json file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Checking for PRODUCT in JSON file. If there isn't, add 0 to the respective product
    for product in json_db:
        if 'quantity' not in product:
            product['quantity'] = 0

    # Converting dict to JSON again, encoding with 'utf8' so the file remains intact
    right_json = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')

    # Overwrite json file with the right quantities
    write_json = open(json_file, 'w', encoding='utf8')
    write_json.write(right_json)

