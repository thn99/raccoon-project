import json

def rightNames(jsonFile):
    wrong_json = open(jsonFile, 'r', encoding='utf8')
    json_db = json.load(wrong_json)

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
        print(product['name'])

rightNames('./broken-database.json')