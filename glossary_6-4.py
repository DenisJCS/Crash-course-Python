glossary = {
    'if':'condition',
    'in':'present',
    'num':'amount',
    'del':'delete',
    'sort':'from a to z',
    'sort revers':'backword',
    'upper':'high register',
    'lower':'lower register',
    'for':'loop',
    'elif':"second if",
    'list':'create a list'
}
for term,definition in glossary.items():
    print("\nTerm:"+term)
    print("Definition:"+definition)
for term,definition in glossary.items():
    print(term.title() + " :definition is "+ definition.title()+".\n")
#only keys
for term in glossary.keys():
    print(term.title())
stared =['upper','lower']
for term in glossary.keys():
    print(term.title())
    if term in stared:
        print("This terms "+term.title()+ " are about register of letters")
#presence in dictionary
if 'set' not in glossary.keys():
    print("Not in this list yet!")
#Put dictionary's output in order
for terms in sorted(glossary.keys()):
    print(terms.title())
#Recieve onlu values
print("For following definitions have been given terms")
for definition in glossary.values():
    print(definition.upper())
#Making sure there is no repeating values
print("The following definitions have been mantioned:")
for definition in set(glossary.values()):
    print(definition.title())
    
