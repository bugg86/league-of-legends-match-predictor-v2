import model as Model
import time
import sys

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
    path = "data/Summoners/{name}/matches/matches.json".format(name=name)
    if Model.check_file(path) :
        match_list = Model.read_json(path)
        for match in match_list :
            Model.get_match(name, match)
    else :
        print("No match list found for {name}".format(name=name))
        
# Generate match dataset for a given user.
def generate_match_dataset(name):
    path = "data/Summoners/{name}/matches/matches.json".format(name=name)
    matchCount = 1
    participantCount = 1
    apiCallsMade = 1
    
    participantNames = [] # This will be used to wipe data from the data/Summoners/ folder in the future.
    
    if Model.check_file(path) :
        match_list = Model.read_json(path)
        for match in match_list :
            matchDataset = Model.read_json('data/matchDataset.json')
            entry = {}
            startTime = time.time()
            
            path = "data/Summoners/{name}/matches/{matchid}.json".format(name=name, matchid=match)
            matchData = Model.read_json(path)
            info = matchData['info']
            if (info['mapId'] != 11) :
                print("Match {matchCount} is not on Summoner's Rift. Skipping...")
                continue
            
            participants = Model.m_get_match_participants(name, match)
            try :
                for participant in participants :
                    # Parse the object for all the data.
                    puuid = Model.m_get_participant_puuid(participant)
                    summonerName = Model.m_get_summoner_name(participant)
                    if (Model.check_dir('data/Summoners/{name}'.format(name=summonerName)) == False) :
                        Model.get_summoner_by_puuid(puuid)
                    print(summonerName)
                    summonerRank = Model.get_summoner_rank_score(summonerName)
                    summonerWinRate = Model.get_summoner_winrate(summonerName)
                    summonerLevel = Model.get_summoner_level(summonerName)
                    teamId = Model.m_get_team_id(participant)
                    championName = Model.m_get_champion_name(participant)
                    championId = Model.m_get_champion_id(participant)
                    championMastery = Model.get_champion_mastery_level(summonerName, championId)
                    spell1 = Model.m_get_summoner_spell_name_1(participant)
                    spell2 = Model.m_get_summoner_spell_name_2(participant)

                    # Store data in entry object.
                    entry['Summoner{count}Name'.format(count=participantCount)] = summonerName
                    entry['Summoner{count}Rank'.format(count=participantCount)] = summonerRank
                    entry['Summoner{count}WinRate'.format(count=participantCount)] = summonerWinRate
                    entry['Summoner{count}Level'.format(count=participantCount)] = summonerLevel
                    entry['Summoner{count}TeamId'.format(count=participantCount)] = teamId
                    entry['Summoner{count}ChampionName'.format(count=participantCount)] = championName
                    entry['Summoner{count}ChampionMastery'.format(count=participantCount)] = championMastery
                    entry['Summoner{count}Spell1'.format(count=participantCount)] = spell1
                    entry['Summoner{count}Spell2'.format(count=participantCount)] = spell2

                    # Store rune data in entry object.
                    runeCount = 1
                    runes = Model.m_get_runes(participant)
                    for rune in runes :
                        if (int(rune) - 8000) > 0 :
                            runeName = Model.get_rune_name(rune)
                            entry['Summoner{count}Rune{runeCount}Name'.format(count=participantCount, runeCount=runeCount)] = runeName
                            runeCount += 1

                    participantCount += 1
            except :
                print(sys.exc_info()[0])
                print('Waiting 90 seconds as a precaution to prevent going over api request limit.')
                time.sleep(90)
                continue
            
            participantCount = 1 # Reset participant count for next match.
            
            #Save match to file in case of interrupt during loop.
            matchDataset.append(entry)
            Model.dump_json('data/matchDataset.json', matchDataset)
            matchDataset = Model.read_json('data/matchDataset.json')
            
            # Sleep for 40 seconds and print out runtime.
            endTime = time.time()
            print('Runtime is {:.3f}s to generate match {count}.'.format((endTime - startTime), count=matchCount))
            if (matchCount == len(match_list)) :
                print('Successfully added {count} matches to matchDataset.json.'.format(count=matchCount))
                break
            else :
                waitTime = 37 - (int(endTime - startTime)) + 1
                print('Waiting for {waitTime} seconds before generating next match.'.format(waitTime=waitTime))
                time.sleep(waitTime)
                
            matchCount += 1
            
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
                entry['Summoner{count}Rune{runeCount}Name'.format(count=count, runeCount=runeCount)] = runeName
                runeCount += 1
        
        count += 1
    
    Model.dump_json('data/entry.json', entry)
    return entry