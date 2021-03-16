available_toppings = ['peppers', 'mushrooms', 'sausages']
requested_toppings = ['bacon', 'peppers', 'mushrooms']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'adding {requested_topping} on your pizza!')
    else:
        print(f"sorry, we don't have {requested_topping} right now.")
print('finished your pizza!')
