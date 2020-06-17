def update_age(dog_owners, owner, new_age):
    if owner in dog_owners and owner[2] != new_age:
        dog_owners[(owner[0], owner[1], int(new_age))] = dog_owners.get(owner)
        dog_owners.pop(owner)
    print(dog_owners)

dog_owners = {("John", "Malkovic", 22): ["Fido"], ("Jake", "Smirnoff", 18): ["Butch"],
("Simon", "Ng", 32): ["Zooma", "Rocky"], ("Martha", "Black", 73): ["Chase"]}

update_age(dog_owners, ('Jake', "Smirnoff", 18), 20)