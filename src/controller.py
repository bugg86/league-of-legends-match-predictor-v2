from api import RiotApi
import json
import os
import consts as Consts

key = 'RGAPI-f84a553c-ba58-45d6-ae7a-ef9c5b31b137'
na1_api = RiotApi(key, Consts.REGIONS['north_america'])
americas_api = RiotApi(key, Consts.REGIONS['americas'])

# Make api call to get summoner.json.
def get_summoner(name) :
    summoner = na1_api.get_summoner_by_name(name)
    validation = error_check(summoner)
    if validation == 'good response' :
        save_summoner(summoner, name)
    else :
        print('Could not write file due to an api call error. Please see response message below:')
        print(validation)
    
# Save summoner.json.
def save_summoner(summoner, name) :
    path = os.path.join('data/', name) #Define player data path.
    # Create player directory if it does not already exist.
    if check_dir(path) != True :
        os.mkdir(path)
        json_summoner = json.dumps(summoner, indent=4)
        with open(os.path.join(path, 'summoner.json'), 'x') as outfile :
            outfile.write(json_summoner)
        outfile.close()
    else :
        print('Player folder already exists.')

# Make api call to get account.json.
def get_account(name) :
    puuid = get_summoner_puuid_by_name(name)
    if puuid != 'Invalid Request' :
        account = americas_api.get_account_by_puuid(puuid)
        #save_account(account, name)
        validation = error_check(account)
        if validation == 'good response' :
            save_account(account, name)
        else :
            print('Could not write file due to an api call error. Please see response message below:')
            print(validation)
    else :
        print('Summoner.json has not been generated for the requested user.')

# Save account.json
def save_account(account, name) :
    path = 'data/' + name + '/account.json'
    if check_file(path) != True :
        json_account = json.dumps(account, indent=4)
        with open(path, 'x') as outfile :
            outfile.write(json_account)
        outfile.close()
    else :
        print('account.json already exists for the requested user.')

# Make api call to get league.json.
def get_league(name) :
    summonerid = get_encrypted_summoner_id_by_name(name)
    if summonerid != 'Invalid Request' :
        league = na1_api.get_league_by_summoner_id(summonerid)
        validation = error_check(league)
        if validation == 'good response' :
            save_league(league, name)
        else :
            print('Could not write file due to an api call error. Please see response message below:')
            print(validation)
    else :
        print('Summoner.json has not been generated for the requested user.')

# Save league.json.
def save_league(league, name) :
    path = 'data/' + name + '/league.json'
    if check_file(path) != True :
        json_league = json.dumps(league, indent=4)
        with open(path, 'x') as outfile :
            outfile.write(json_league)
        outfile.close()
    else :
        print('league.json already exists for the requested user.')

# Make api call to get champion_mastery.json.
def get_champion_mastery(name) :
    summonerid = get_encrypted_summoner_id_by_name(name)
    if summonerid != 'Invalid Request' :
        champion_mastery = na1_api.get_champ_mastery_by_summoner_id(summonerid)
        validation = error_check(champion_mastery)
        if validation == 'good response' :
            save_champion_mastery(champion_mastery, name)
        else :
            print('Could not write file due to an api call error. Please see response message below:')
            print(validation)
    else :
        print('summoner.json has not been generated for the requested user.')

# Save champion_mastery.json.
def save_champion_mastery(champion_mastery, name) :
    path = 'data/' + name + '/champion_mastery.json'
    if check_file(path) != True :
        json_champion_mastery = json.dumps(champion_mastery, indent=4)
        with open(path, 'x') as outfile :
            outfile.write(json_champion_mastery)
        outfile.close()
    else :
        print('summoner.json already exists for the requested user.')

# Make api call to get live_match.json.
def get_live_match(name) :
    summonerid = get_encrypted_summoner_id_by_name(name)
    if summonerid != 'Invalid Request' :
        live_match = na1_api.get_live_match_by_summoner_id(summonerid)
        validation = error_check(live_match)
        if validation == 'good response' :
            save_live_match(live_match, name)
        else :
            print('Could not write file due to an api call error. Please see response message below:')
            print(validation)
    else :
        print('summoner.json has already been generated for the requested user.')

# Save champion_mastery.json.
def save_live_match(live_match, name) :
    path = 'data/' + name + '/live_match.json'
    json_live_match = json.dumps(live_match, indent=4)
    with open(path, 'x') as outfile :
        outfile.write(json_live_match)
    outfile.close()

# Make api call to get matches.json
def get_match_list(name, start, end) :
    puuid = get_summoner_puuid_by_name(name)
    if puuid != 'Invalid Request' :
        matches = americas_api.get_match_list_by_summoner_id(puuid, start, end)
        validation = error_check(matches)
        if validation == 'good response' :
            save_match_list(matches, name)
        else :
            print('Could not write file due to an api call error. Please see response message below:')
            print(validation)
    else :
        print('summoner.json has already been generated for the requested user.')

# Save matches.json.
def save_match_list(matches, name) :
    dir = 'data/' + name + '/matches'
    if check_dir(dir) != True :
        os.mkdir(dir)
    path = 'data/' + name + '/matches/matches.json'
    json_matches = json.dumps(matches, indent=4)
    with open(path, 'x') as outfile :
        outfile.write(json_matches)
    outfile.close()


#==================UTILITY FUNCTIONS==================#

# Check if directory exists.
def check_dir(path) :
    isdir = os.path.isdir(path)
    if isdir :
        return True
    else :
        return False

# Check if file exists.
def check_file(path) :
    isfile = os.path.isfile(path)
    if isfile :
        return True
    else :
        return False

# Returns puuid based on summoner name.
def get_summoner_puuid_by_name(name) :
    path = 'data/' + name + '/summoner.json'
    # Return puuid if the summoner.json for the requested user exists.
    if check_file(path) :
        summoner = {}
        with open(path) as file :
            summoner = json.load(file)
        file.close()
        return summoner['puuid']
    else :
        return 'Invalid Request'

# Returns encrypted summoner id based on summoner name.
def get_encrypted_summoner_id_by_name(name) :
    path = 'data/' + name + '/summoner.json'
    # Return puuid if the summoner.json for the requested user exists.
    if check_file(path) :
        summoner = {}
        with open(path) as file :
            summoner = json.load(file)
        file.close()
        return summoner['id']
    else :
        return 'Invalid Request'

# Check json response for errors.
def error_check(json_response) :
    if 'status' in json_response :
        status = json_response['status']
        message = status['message']
        status_code = status['status_code']
        return {'message' : message, 'status_code' : status_code}
    else :
        return 'good response'