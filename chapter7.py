name = input("Please enter your name: ")
print(f"\nHello,{name}!")

#greeting
prompt = ("If you share your name, we can personalize this message you see.")
prompt += ("\nWhat is your first name?")

name = input(prompt)
print(f"\nHello, {name}!")

#Using int()
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
#Above Python interprets everything as a string and if we want work only with number we will get type error
#Example below 
>>> age = ("How old are you? ")
>>> 21
21
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
#To have numerical access will use int()
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)  #Here is int()
>>> age >= 18
True
>>> 


rollecoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >=48:
    print("\nYou are tall enough to ride.")
else:
    print("\nYou'll be able to ride, when you're a little older.")
        
#Exercise 7-1
car = input("What kind of car would you like to rent? ")
car_list = ['subaru', 'toyota','mercedes']

if car in car_list:
    print(f"We can provide you with a {car} car !")
else:
    print(f"We don't have this {car} car, please choose other.")

#Exercise 7-2
#Restaurant
lobby = input("How many people are in your group? ")
lobby = int(lobby)
if lobby <=8:
    print("Your table is ready!")
else:
    print("You have to wait for the table")    

#Exercise 7-3 Multiple of 10
 #Exercise 7-3
number = int(input("Enter your number and we will show you if it multiple of 10: "))
if number % 10 == 0:
    print("Your number is multiple of 10")
else:
    print("Not multiple of 10")


#Using (while) loop to run program till the condition is true
#Parrot
prompt = "\nTell me something, I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message !='quit':
    message = input(prompt)
    print(message)
    if message != 'quit':
      print(message)

Tell me something, I will repeat it back to you: 
Enter 'quit' to end the program. yes
yes

Tell me something, I will repeat it back to you: 
Enter 'quit' to end the program. Hello, Deni!
Hello, Deni!

Tell me something, I will repeat it back to you: 
Enter 'quit' to end the program. quit
quit

