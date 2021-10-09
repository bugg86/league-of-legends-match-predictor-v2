import controller as Controller

name = input('Enter summoner name: ')

summoner_option = input('Do you want to generate summoner.json? y/n : ')
if summoner_option == 'y' :
    Controller.get_summoner(name)

league_option = input('Do you want to generate league.json? y/n : ')
if league_option == 'y' : 
    Controller.get_league(name)

champ_mastery_option = input('Do you want to generate champ_mastery.json? y/n : ')
if champ_mastery_option == 'y' :
    Controller.get_champion_mastery(name)

live_match_option = input('Do you want to generate live_match.json? y/n : ')
if live_match_option == 'y' :
    Controller.get_live_match(name)