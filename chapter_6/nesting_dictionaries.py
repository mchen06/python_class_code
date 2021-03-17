dragon_0 = {'color' : 'red', 'name' : 'nidhogg', 'size' : 'large'}
dragon_1 = {'color' : 'red', 'name' : 'fafnir', 'size' : 'medium'}
dragon_2 = {'color' : 'red', 'name' : 'smaug', 'size' : 'massive'}
dragons = [dragon_0, dragon_1, dragon_2]
for dragon in dragons:
    print(dragon)

pizza = {'crust' : 'thick', 'toppings' : ['chicken', 'peperoni', 'sausage']}
print(f'you ordered a pizza with a {pizza["crust"]} crust, '
      "and the following toppings:")
for topping in pizza['toppings']:
    print(f'\t{topping}')
