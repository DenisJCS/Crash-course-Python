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

#Exercise 6-10
numbers = {'Denis':['7','12'],
           'Jessica':['23','17'],
           'Alex':['5','23'],
           'Vadeam':['15','55'],
           'Rita':['10','100'],
           }
for user,numbers in numbers.items():
    print(f"\nUser name is:{user.upper()} and favorite numbers are:")
    for number in numbers:
        print(f"\t{number.title()}")


#Exercise 6-11
cities = {
    'los angeles':{
        'country':'america/usa',
        'population':'10 million',
        'fun fact':'gta 5 was in LA',
    },
    'bishkek':{
        'country':'kyrgyzstan',
        'population':'1.5 million',
        'fun fact':'previous name is Frunze',

    },
    'Seattle':{
        'country':'USA',
        'population':'3.4 million',
        'fun fact':'Homeland of Microsoft',
    },
}    
for info,cities in cities.items():
    print(f"\nName of city:{info.upper()}")
    print(f"\tLocation in: {cities['country']},\n"
          f"\tPopulation:{cities['population']}\n"
          f"\tFun fact about this city: {cities['fun fact']}")

#Exercise 6-12people = {
people ={
    'lsumrall':{
        'first':'lester',
        'last':'sumrall',
        'born':'lousiana',
        'job':'preacher',
        'location':'pensecola',
    },
    'ccarnegy':{
        'first':'dale',
        'last':'carnegy',
        'born':'new york',
        'job':'eunterprenuer',
        'location':'penselvania',
    },
}
#Adding new key,value(manualy)
people['lsumrall']['wife'] = 'louise layman'
people['ccarnegy']['wife']='louise whitfield'
#Adding new kay,value in both dict
key = 'nation'
value = 'american'
#changing value
people['lsumrall']['job']='evengalist'

for inner_dict in people.values():
    inner_dict[key] = value
    print(people)
for username,user_info in people.items():
    print(f"\nUsername :{username}")
    full_name_nation = f"{user_info['first']} {user_info['last']} {user_info['nation']}"
    born_job = f"{user_info['born']+":"} {user_info['job']}"
    location = user_info['location']
    print(f"\tFull name and nation:{full_name_nation.title()}")
    print(f"\tWife : {user_info['wife'].title()}")
    print(f"\tBorn and job:{born_job.title()}")
    print(f"\tLocation:{location.title()}")
#del key
del people['ccarnegy']['wife']
print(people['ccarnegy'])
#pop key
people['lsumrall'] .pop('born')
print(people['lsumrall'])
#changing value in dict
people['ccarnegy']['born']='tennesy'
print(people['ccarnegy'])

    
