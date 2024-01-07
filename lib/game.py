from game_data import *

def get_all_players():
    data = game_dict()
    home =  data["home"]["players"]
    away = data["away"]["players"]
    return home + away

def num_points_per_game(name):
    players = get_all_players()

    for i in players:
        if i["name"] == name:
            return i["points_per_game"]
    
def player_age(name):
    players = get_all_players()

    for i in players:
        if i["name"] == name:
            return i["age"]

def team_colors(name):
    data = game_dict()
    if data["home"]["team_name"] == name:
        return data["home"]["colors"]
    
    return data["away"]["colors"]

def team_names():
    data = game_dict()
    
    names = [data[team]["team_name"] for team in data]
    print(names)

def player_numbers(name):
    data = game_dict()
    if data["home"]["team_name"] == name:
        return [player["number"] for player in data["home"]["players"]]
    
    return [player["number"] for player in data["away"]["players"]]

        
def player_stats(name):
    data = get_all_players()

    for player in data:
        if player["name"] == name:
            return player
    


