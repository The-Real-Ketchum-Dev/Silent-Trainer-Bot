import sys
import json
def get_poke_info():
    try:
        with open('cogs/pokemon.json') as data_file:
            data = json.load(data_file)
    except:
        print('Fatal Error, JSON file missing!')
        sys.exit()

    return data

def get_badge_info():
    try:
        with open('data/badges/badges.json') as data_file:
            data = json.load(data_file)
    except:
        print('Fatal Error, JSON file missing!')
        sys.exit()

    return data