import json

def add_coordinates(file_name: str):
    '''
    Adds coordinates to each text pattern in json object.
    '''
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

    for pattern in data['texts']:
        x = (pattern['column_min'] + pattern['column_max']) / 2
        y = (pattern['row_min'] + pattern['row_max']) / 2
        pattern['coordinates'] = (x, y)

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

add_coordinates('screenshot.json')

