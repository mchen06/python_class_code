dog = {'name' : 'onyx', 'color' : 'black'}
print(dog['name'])
print(dog['color'])

dog['trick'] = 'sit'
print(dog)
dog['trick'] = 'shake'
print(dog)
del dog['trick']
print(dog)

dog_name = dog['name'].title()
tricks = dog.get('trick', f'{dog_name} knows no tricks')
print(tricks)
