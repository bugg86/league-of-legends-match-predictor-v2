import model as Model

name = input('Enter summoner name: ')

# print(Model.get_summoner_winrate(name))
print(Model.get_summoner_level(name))
Model.get_match(name, 'NA1_4065555392')

# summoner_option = input('Do you want to generate summoner.json? y/n : ')
# if summoner_option == 'y' :
#     Model.get_summoner(name)

# league_option = input('Do you want to generate league.json? y/n : ')
# if league_option == 'y' : 
#     Model.get_league(name)

# champ_mastery_option = input('Do you want to generate champ_mastery.json? y/n : ')
# if champ_mastery_option == 'y' :
#     Model.get_champion_mastery(name)

# live_match_option = input('Do you want to generate live_match.json? y/n : ')
# if live_match_option == 'y' :
#     Model.get_live_match(name)

# matches_option = input('Do you want to generate matches.json? y/n : ')
# count = int(input('How many matches? Enter number: '))
# if matches_option == 'y' :
#     Model.get_match_list(name, 0, count)