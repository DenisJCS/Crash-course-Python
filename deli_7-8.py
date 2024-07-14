#Code below
sandwich_orders = ['tuna', 'meatballs', 'vegeterian', 'chicken tender']
finished_sandwiches = []
order = True
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"We are preparing your :{current_order.title()} sandwich" )
    finished_sandwiches.append(current_order)
print("\nFollowing orders are ready !")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich.title()} sandwich is ready")
