def players_by_position(squads_list):
    players_by_position = {}
    for player in squads_list:
        position = player['position']
        if position not in players_by_position:
            players_by_position[position] = []
        players_by_position[position].append(player)
    return players_by_position