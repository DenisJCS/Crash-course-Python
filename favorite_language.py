favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'alex':'js',
 }
print("Sarah's favorite language is "+
      favorite_languages['sarah'].title()+".")
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is " +str(language)+".")

for key,value in favorite_languages.items():
    print("\nKey:"+key)
    print("Value:"+value)

for name,language in favorite_languages.items():
    print(name.title()+" s favorite language is "+language.title())

for name in favorite_languages.keys():
    print(name.title())
#Take all names from the dictionary
#and when right name appears will show the message
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title()+ 
              ", I see your favorite language is "+
              favorite_languages[name].title()+"!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# Recieving keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title()+ ",thank you for taking the poll")
#Recieving value without keys
print("The following languages have been mantioned:")
for language in favorite_languages.values():
    print(language.title())

#Nesting multiple lists into dictionary
# Putting two list values into dictionary
favorite_languages = {
    'jen':['python', 'rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskel'],
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
