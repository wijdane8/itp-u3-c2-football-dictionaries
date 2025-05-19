def players_by_country_and_position(squads_list):
    players_by_country_and_position = {}
    for player in squads_list:
        country = player['country']
        position = player['position']
        if country not in players_by_country_and_position:
            players_by_country_and_position[country] = {}
        if position not in players_by_country_and_position[country]:
            players_by_country_and_position[country][position] = []
        players_by_country_and_position[country][position].append(player)
    return players_by_country_and_position
