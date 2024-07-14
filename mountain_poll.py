#Filling a dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store responses in  the dictionary
    responses[name] = response
    #Find out if anyone else is going to take a poll.
    repeat = input("Would you like to let  another person respond ? (yes/no)? ")
    if repeat == 'no':
        polling_active = False
#Polling is completed. Show the resilts.
print("\n ---Poll Resuld ---")
for name,response in responses.items():
    print(f"{name} would like tp climb {response}. ")
    