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
