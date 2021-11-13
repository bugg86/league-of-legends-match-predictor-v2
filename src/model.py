from api import RiotApi
import json
import os
import consts as Consts

key = 'RGAPI-9ff68402-d7eb-4ff8-83e3-084a05db7866'
na1_api = RiotApi(key, Consts.REGIONS['north_america'])
americas_api = RiotApi(key, Consts.REGIONS['americas'])

#========================JSON GENERATION FUNCTIONS========================#

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
    path = 'data/Summoners/{name}/'.format(name=name) #Define player data path.
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
    path = 'data/Summoners/{name}/account.json'.format(name=name)
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
    path = 'data/Summoners/{name}/league.json'.format(name=name)
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
    path = 'data/Summoners/{name}/champion_mastery.json'.format(name=name)
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
    path = 'data/Summoners/{name}/live_match.json'.format(name=name)
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
    dir = 'data/Summoners/{name}/matches'.format(name=name)
    if check_dir(dir) != True :
        os.mkdir(dir)
    path = 'data/' + name + '/matches/matches.json'
    json_matches = json.dumps(matches, indent=4)
    with open(path, 'x') as outfile :
        outfile.write(json_matches)
    outfile.close()

# Make api call to get {matchid}.json.
def get_match(name, matchid) :
    match = americas_api.get_match_by_match_id(matchid)
    validation = error_check(match)
    if validation == 'good response' :
        save_match(match, name, matchid)
    else :
        print('Could not write file due to an api call error. Please see response message below:')
        print(validation)

# Save {matchid}.json.
def save_match(match, name, matchid) :
    dir = 'data/Summoners/{name}/matches'.format(name=name)
    if check_dir(dir) != True :
        os.mkdir(dir)
    path = 'data/Summoners/{name}/matches/{matchid}.json'.format(name=name, matchid=matchid)
    json_match = json.dumps(match, indent=4)
    with open(path, 'x') as outfile :
        outfile.write(json_match)
    outfile.close()

# Generate summoner.json, league.json, and champion_mastery.json for a given summoner.
def generate_summoner_json(name) :
    get_summoner(name)
    get_league(name)
    get_champion_mastery(name)



#==================JSON PARSING FUNCTIONS==================#

# Parse summoner.json to get summoner level.
def get_summoner_level(name) :
    path = 'data/Summoners/{name}/summoner.json'.format(name=name)
    summoner = {}
    if check_file(path) == True :
        with open(path, 'r') as infile :
            summoner = json.load(infile)
        infile.close()
    else :
        print('summoner.json does not exist for the requested user, generating summoner files.')
        generate_summoner_json(name)
        with open(path, 'r') as infile :
            summoner = json.load(infile)
        infile.close()

    return summoner['summonerLevel']

# Parse league.json and calculate winrate.
def get_summoner_winrate(name) :
    path = 'data/Summoners/{name}/league.json'.format(name=name)
    league = {}
    if check_file(path) == True :
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()
    else :
        print('league.json does not exist for the requested user, generating summoner files.')
        generate_summoner_json(name)
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()

    wins = league['wins']
    losses = league['losses']

    return float((wins / losses) * 100)

# Parse league.json and the scoring json files to get numerical value for rank.
def get_summoner_rank_score(name) :
    path = 'data/Summoners/{name}/league.json'.format(name=name)
    league = {}
    if check_file(path) == True :
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()
    else :
        print('league.json does not exist for the requested user, generating summoner files.')
        generate_summoner_json(name)
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()

    tier = league['tier']
    division = league['rank']
    # Get the score for the tier.
    path = 'data/rank_tier_scoring.json'
    json_tier_scoring = {}
    with open(path, 'r') as infile :
        json_tier_scoring = json.load(infile)
    infile.close()
    tierscore = json_tier_scoring[tier]
    # Get the score for the division.
    path = 'data/rank_division_scoring.json'
    json_division_scoring = {}
    with open(path, 'r') as infile :
        json_division_scoring = json.load(infile)
    infile.close()
    divisionscore = json_division_scoring[division]
    
    return tierscore + divisionscore


# Parse league.json and return a concat of the tier and division for the summoner's rank.
def get_summoner_rank(name) :
    path = 'data/Summoners/{name}/league.json'.format(name=name)
    league = {}
    if check_file(path) == True :
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()
    else :
        print('league.json does not exist for the requested user, generating summoner files.')
        generate_summoner_json(name)
        with open(path, 'r') as infile :
            temp = json.load(infile)
            league = temp[0]
        infile.close()

    tier = league['tier']
    division = league['division']
    return str(tier + ' ' + division)

# Parse summoner_spells.json to get the summoner spell name using the id.
def get_summoner_spell_name(id) :
    name = ''
    with open('data/summoner_spells.json', 'r') as infile :
        temp = json.load(infile)
        name = temp[str(id)]
    infile.close()

    return str(name)

# Parse champions.json to get the champion name using the id.
def get_champion_name(id) :
    name = ''
    with open('data/champions.json', 'r') as infile :
        temp = json.load(infile)
        name = temp[str(id)]
    infile.close()

    return str(name)


# Parse champion_mastery.json to get champion mastery level given an id.
def get_champion_mastery_level(name, id) :
    path = 'data/Summoners/{name}/champion_mastery.json'.format(name=name)
    champion_mastery = []
    championLevel = 0
    if check_file(path) == True :
        with open(path, 'r') as infile :
            champion_mastery = json.load(infile)
        infile.close()
    else :
        print('champion_mastery.json does not exist for the requested user, generating summoner files.')
        generate_summoner_json(name)
        with open(path, 'r') as infile :
            champion_mastery = json.load(infile)
        infile.close()

    for champion in champion_mastery :
        if champion['championId'] == id :
            championLevel = champion['championLevel']
            break
    return championLevel

# Parse runes.json to get rune name given an id.
def get_rune_name(id) :
    name = ''
    with open('data/runes.json', 'r') as infile :
        temp = json.load(infile)
        name = temp[str(id)]
    infile.close()

    return str(name)


#==================PARSE LIVE MATCH JSON==================#

# Get participants array from live_match.json.
def lm_get_live_match_participants(name) : 
    path = 'data/Summoners/{name}/live_match.json'.format(name=name)
    live_match = {}
    if check_file(path) == True :
        with open(path, 'r') as infile :
            live_match = json.load(infile)
        infile.close()
    else :
        print('live_match.json does not exist for the requested user.')
    participants = live_match['participants']

    return participants

# Get summoner spell id 1 from participant object from participants array.
def lm_get_summoner_spell_name_1(participant) :
    return get_summoner_spell_name(participant['spell1Id'])

# Get summoner spell id 2 from participant object from participants array.
def lm_get_summoner_spell_name_2(participant) :
    return get_summoner_spell_name(participant['spell2Id'])

# Get champion id from participant object from participants array.
def lm_get_champion_id(participant) :
    return participant['championId']

# Get champion name from participant object from participants array.
def lm_get_champion_name(participant) :
    return get_champion_name(participant['championId'])

# Get summoner name from participant object from participants array.
def lm_get_summoner_name(participant) :
    return participant['summonerName']

# Get team id from participant object from participants array.
def lm_get_team_id(participant) :
    return participant['teamId']

# Get rune array from participant object from participants array.
def lm_get_runes(participant) :
    perks = participant['perks']
    return perks['perkIds']



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
    path = 'data/Summoners/{name}/summoner.json'.format(name=name)
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
    path = 'data/Summoners/{name}/summoner.json'.format(name=name)
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
    
# Dump json to specified file path.
def dump_json(path, data) :
    with open(path, 'w') as outfile :
        json.dumps(data, outfile, indent=4)
    outfile.close()