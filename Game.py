def get_objects_by_coords(position):
    return [key for key, value in game_objects.items() if value['position'] == position]


def remove_objects():
    for i in old_objects:
        game_objects.pop(i, [])
    old_objects.clear()


def player_interaction(player, obj):
    if obj[0] == 'coin': old_objects.append(obj)


def wave_interaction(wave, obj):
    if obj[0] in ['player', 'soft_wall']: old_objects.append(obj)


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}
old_objects = [('player',)]
