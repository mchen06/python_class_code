print('welcome to the movie theater!')
party = []
finished = "yes"
while finished != 'no':
    age = input("\nwhat's your age?")
    age = int(age)
    if age <= 3:
        print("\nyour ticket is free!")
    elif age <= 12 and age > 3:
        party.append('ten')
        print("\nyour ticket costs $10!")
    else:
        party.append('fifteen')
        print("\nyour ticket costs $15!")
    finished = input("\nis there anybody else in your party? (yes/no)")
ten_dollar = party.count('ten') * 10
fifteen_dollar = party.count('fifteen') * 15
total = ten_dollar + fifteen_dollar
print(f"your total is ${total}!")
