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
        
