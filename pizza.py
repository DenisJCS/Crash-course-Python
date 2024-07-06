#Store information about pizza bring ordered
pizza = {
    'crust':'thick',
    'topping':['mushroom', 'extra chese'],
    }
#Summarize the order.
print(f"You ordered a {pizza['crust']}- crust pizza \n"
      "with a following toppings:")
for topping in pizza['topping']:
    print(f"\t{topping}")
