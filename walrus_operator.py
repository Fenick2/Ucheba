animals = ['dog', 'lion', 'bear', 'tiger']
for animal in animals:
    if (len_animal := len(animal)) > 4:
        print(f'The animal “{animal}” has “{len_animal}”, letters!')