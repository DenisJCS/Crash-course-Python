pets = {
    'dog':{
        'animal':'dog',
        'kind':'ovcharka',
        'name':'jairan',
        'age':4,
        'owner':'alex',
        'location':'vilige',
    },
    'horse':{
        'animal':'horse',
        'kind':'mountain',
        'name':'maximus',
        'age':5,
        'owner':'luke',
        'location':'farm',
    },
    
}
for pet,pets_info in pets.items():
    print(f"\nPet : {pet}")
    animal_info = f"{pets_info['animal']} {pets_info['kind']}"
    name_age = f"{pets_info['name']+":"} {pets_info['age']}"
    owner = f"{pets_info['owner']}"
    location = f"{pets_info['location']}"
    print(f"\tAnimal info : {animal_info.title()}")
    print(f"\tName and age of animal :{name_age.title()}")
    print(f"\tOwner is : {owner.title()}")
    print(f"\tLocation is :{location.title()}")
print("Well done , exercise 6-8 is done")


#Exercise 6-9
friends = {
    'friend':{
        'name':'joshua',
        'first':'time square',
        'second':'silver lake',
        'third':'baikal',
    },
    'friend_2':{
        'name':'monica',
        'first':'downtown',
        'second':'old castle',
        'third':'roma',
    },
}
for user,friends in friends.items():
    print(f"\nName of friend is:{user.title()}")
    print(f"Name is :{friends['name'].title()}")
    favorite_places = f"{friends['first']+":"}{friends['second']+":"}{friends['third']}"
    print(f"\t Favorite places:{favorite_places.title()} ")

