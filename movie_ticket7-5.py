#This code receives age(number) and according that gives price for movie ticket

active  = True
while active:
    age_input = input("Please enter your age and we will count the cost (or enter 'quit' to stop): ")

    if age_input.lower() == 'quit':
        active = False
    else:
        try:
            age = int(age_input)
            if age <=3:
                print("Your ticket is free !")
            elif 3< age <12:    
                print("Your ticket costs $10.")
            else:
                print("Your ticket costs $15.")
        except ValueError:
            print("Please enter valid number")         

