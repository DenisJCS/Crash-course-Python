prompt = "\nPlese choose toppings for your pizza.: "
prompt += "\nEnter 'quit' to finish: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
     print(f"You added this topping {message.title()}")

