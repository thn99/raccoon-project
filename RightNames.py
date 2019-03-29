import json


def right_names(json_file):
    # Loading json file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Checking for incorrect characters in all product names. If there is, replace for the right character
    # Also checks if it is or isn't a capital character
    for product in json_db:
        if 'name' in product:
            old_name = str(product['name'])
            new_name = ''
            for i in range(len(old_name)):
                if old_name[i] == 'æ':
                    if old_name[i - 1] == ' ':
                        new_name += 'A'
                    else:
                        new_name += 'a'

                elif old_name[i] == '¢':
                    if old_name[i - 1] == ' ':
                        new_name += 'C'
                    else:
                        new_name += 'c'

                elif old_name[i] == 'ø':
                    if old_name[i - 1] == ' ':
                        new_name += 'O'
                    else:
                        new_name += 'o'
                elif old_name[i] == 'ß':
                    if old_name[i - 1] == ' ':
                        new_name += 'B'
                    else:
                        new_name += 'b'
                else:
                    new_name += old_name[i]
                product['name'] = new_name

    # Converting dict to JSON again, encoding with 'utf8' so the file remains intact
    right_json = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')

    # Overwrite json file with the right prices
    write_json = open(json_file, 'w', encoding='utf8')
    write_json.write(right_json)
