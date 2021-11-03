import csv
import os
import model as Model
import json

# Get user input.
def get_user_input_name():
    return input("Enter a summoner name: ")


#============SUMMONER DATA GENERATION FUNCTIONS============#

# Generate all summoner related json files.
def generate_all_summoner_json(name):
    generate_summoner_json(name)
    generate_league_json(name)
    generate_champion_mastery_json(name)

# Generate summoner.json for a given summoner name.
def generate_summoner_json(name):
    Model.get_summoner(name)

# Generate league.json for a given summoner name.
def generate_league_json(name):
    Model.get_league(name)

# Generate champion_mastery.json for a given summoner name.
def generate_champion_mastery_json(name):
    Model.get_champion_mastery(name)


#============MATCH DATA GENERATION FUNCTIONS============#

# Generate match list for a given summoner name with a start and end index.
def generate_match_list(name, start, end):
    Model.get_match_list(name, start, end)

# Generate 'matchid'.json for a given user if their match_list.json exists.
def generate_matches_json(name):
    path = "data/{name}/matches/matches.json".format(name=name)
    if Model.check_file(path) :
        with open(path, 'r') as f :
            match_list = json.load(f)
        f.close()
        for match in match_list :
            Model.get_match(name, match)
    else :
        print("No match list found for {name}".format(name=name))


#============LIVE MATCH DATA GENERATION FUNCTIONS============#

# Generate live_match.json for a given summoner name.
def generate_live_match_json(name):
    Model.get_live_match(name)

# Generate all live match json entry.
def generate_live_match_entry_for_submission(name):
    participants = Model.lm_get_live_match_participants(name)
    count = 1
    entry = {}
    for participant in participants :
        summonerName = Model.lm_get_summoner_name(participant)
        print(summonerName)
        summonerRank = Model.get_summoner_rank_score(summonerName)
        summonerWinRate = Model.get_summoner_winrate(summonerName)
        summonerLevel = Model.get_summoner_level(summonerName)
        teamId = Model.lm_get_team_id(participant)
        championName = Model.lm_get_champion_name(participant)
        championId = Model.lm_get_champion_id(participant)
        championMastery = Model.get_champion_mastery_level(summonerName, championId)
        spell1 = Model.lm_get_summoner_spell_name_1(participant)
        spell2 = Model.lm_get_summoner_spell_name_2(participant)

        entry['Summoner{count}Name'.format(count=count)] = summonerName
        entry['Summoner{count}Rank'.format(count=count)] = summonerRank
        entry['Summoner{count}WinRate'.format(count=count)] = summonerWinRate
        entry['Summoner{count}Level'.format(count=count)] = summonerLevel
        entry['Summoner{count}TeamId'.format(count=count)] = teamId
        entry['Summoner{count}ChampionName'.format(count=count)] = championName
        entry['Summoner{count}ChampionMastery'.format(count=count)] = championMastery
        entry['Summoner{count}Spell1'.format(count=count)] = spell1
        entry['Summoner{count}Spell2'.format(count=count)] = spell2
        
        runeCount = 1
        runes = Model.lm_get_runes(participant)
        for rune in runes :
            if (rune - 8000) > 0 :
                runeName = Model.get_rune_name(rune)
                runeCount += 1
                entry['Summoner{count}Rune{runeCount}Name'.format(count=count, runeCount=runeCount)] = runeName
        
        count += 1
    
    with open('data/entry.json', 'w') as f :
        json.dump(entry, f, indent=4)
    f.close()
    return entry