game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}

def get_objects_by_coords(position):
    return [k for k, v in game_objects.items() if v['position'] == position]



print(get_objects_by_coords((0, 1)) == [('wall', 1)])
print(get_objects_by_coords((1, 1)) == [('player',)])
print(get_objects_by_coords((2, 1)) == [])
