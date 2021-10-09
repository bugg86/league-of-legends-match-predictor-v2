import requests
import consts as Consts

key = 'RGAPI-34c449af-c9ef-49c2-af46-46eae22151f2'

class RiotApi(object) :
    def __init__(self, api_key, region) :
        self.api_key = api_key
        self.region=region

    def request(self, api_url, params={}) :
        args = {'api_key' : self.api_key}
        for key, value in params.items() :
            if key not in args :
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
            ), 
            params = args
        )
        # print (response.url)
        return response.json()
    
    # Look up summoner information using their summoner name.
    def get_summoner_by_name(self, name) :
        api_url = Consts.URL['summoner_by_name'].format(
            version = Consts.API_VERSIONS['summoner'],
            name=name
        )
        return self.request(api_url)

    # Look up account information using puuid.
    def get_account_by_puuid(self, puuid) :
        api_url = Consts.URL['account_by_puuid'].format(
            version = Consts.API_VERSIONS['account'],
            puuid = puuid
        )
        return self.request(api_url)

    # Look up league information using encrypted summoner id.
    def get_league_by_summoner_id(self, summonerid) :
        api_url = Consts.URL['league_by_summoner_id'].format(
            version = Consts.API_VERSIONS['league'],
            summonerID = summonerid
        )
        return self.request(api_url)

    # Look up champion mastery information using encrypted summoner id.
    def get_champ_mastery_by_summoner_id(self, summonerid) :
        api_url = Consts.URL['champion_mastery_by_summoner_id'].format(
            version = Consts.API_VERSIONS['champion-mastery'],
            summonerID = summonerid
        )
        return self.request(api_url)