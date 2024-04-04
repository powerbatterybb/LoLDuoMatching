import requests

def rank_list():

    user_url = 'https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/{}/I?page={}&api_key={}'
    tiers = ['CHALLENGER']
    my_api = 'RGAPI-e7a36c70-1087-4375-a749-3c21660c1af5'
    url_now = user_url.format('CHALLENGER', 1, my_api)
    reqq = requests.get(url_now).json()


    return(reqq)