import csv
import os
import model as Model
import json

# Get user input.
def get_user_input_name():
    return input("Enter a summoner name: ")


#============DATA GENERATION FUNCTIONS============#

# Generate summoner.json for a given summoner name.
def generate_summoner_json(name):
    Model.get_summoner(name)

# Generate league.json for a given summoner name.
def generate_league_json(name):
    Model.get_league(name)

# Generate champion_mastery.json for a given summoner name.
def generate_champion_mastery_json(name):
    Model.get_champion_mastery(name)

# Generate live_match.json for a given summoner name.
def generate_live_match_json(name):
    Model.get_live_match(name)

# Generate match list for a given summoner name with a start and end index.
def generate_match_list(name, start, end):
    Model.get_match_list(name, start, end)

# Generate 'matchid'.json for a given user if their match_list.json exists.
def generate_matches_json(name):
    path = "data/{name}/matches.json".format(name=name)
    if Model.check_file(path) :
        with open(path, 'r') as f :
            match_list = json.load(f)
        f.close()
        for match in match_list :
            Model.get_match(name, match)

# This function will make calls to the model to generate an array that will be written to a csv file.
def generate_live_match_data(name):
    return ""