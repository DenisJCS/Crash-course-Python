#Code below
responses = {}
dream_poll = True
while dream_poll:
    name = input("\nWhat is your first name ? ")
    response = input("\nIf you could visit one place in the world, where would ypu go ? ")
    responses[name]= response
    repeat = input("If you want to stop enter ('stop') ")
    if repeat == 'stop':
     dream_poll = False
print("---Polling results---")
for name,response in responses.items():
    print(f" {name.title()} would like to visit {response.title()}")

