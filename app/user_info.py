import requests
import csv
from app import app

def get_user_data(steam_id):
    '''
    Creates a csv file called training_data with the format: (steamid,gameid,play_time)

    '''
    g_api = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + app.config['STEAM_API_KEY'] + '&steamid=' + str(steam_id) + '&format=json'
    output = []
    game_data = requests.get(g_api).json()
    print(len(filter_unplayed(game_data)))
    with open('training_data','w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in game_data['response']['games']:
            writer.writerow([steam_id,i['appid'],i['playtime_forever']])

def filter_unplayed(game_data):
    unplayed_games = []
    for i in game_data['response']['games']:
        if i['playtime_forever'] == 0:
            unplayed_games.append(i['appid'])
    return unplayed_games
