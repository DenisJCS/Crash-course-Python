#Code below
sandwich_orders = ['pastrami','tuna', 'meatballs','pastrami', 'vegetarian', 'chicken tender','pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry we do not have pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"We are preparing your :{current_order.title()} sandwich" )
    finished_sandwiches.append(current_order)
print("\nFollowing orders are ready !")

for sandwich in finished_sandwiches:
    print(f"Your {sandwich.title()} sandwich is ready")
