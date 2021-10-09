import controller as Controller

name = input('Enter summoner name: ')

summoner_option = input('Do you want to generate summoner.json? y/n : ')
if summoner_option == 'y' :
    Controller.get_summoner(name)

league_option = input('Do you want to generate league.json? y/n : ')
if league_option == 'y' : 
    Controller.get_league(name)