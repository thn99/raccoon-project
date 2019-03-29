import json


def right_names(json_file):
    # Loading JSON file
    json_db = json.load(open(json_file, 'r', encoding='utf8'))

    # Checking for wrong characters, correcting them and checking if the changed characters
    # are capital characters
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

    write_json = open(json_file, 'w', encoding='utf8')
    # Encoding (in order to prevent having problems with wrong characters) and transforming python dict to JSON
    right_file = json.dumps(json_db, indent=5, ensure_ascii=False).encode('utf8').decode('utf8')
    # Overwriting corrections to file
    write_json.write(right_file)


# Calling functions
right_names('./broken-database.json')