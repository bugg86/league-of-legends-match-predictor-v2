import os
import json

def do_shit() :
    runes = []
    new_runes = {}
    with open('data/runesReforged.json', 'r') as infile :
        runes = json.load(infile)
    infile.close()

    for rune in runes :
        key = rune["id"]
        name = rune["key"]
        new_runes[key] = name

    json_runes = json.dumps(new_runes, indent=4)
    with open('data/runes.json', 'x') as outfile:
        outfile.write(json_runes)
    outfile.close()