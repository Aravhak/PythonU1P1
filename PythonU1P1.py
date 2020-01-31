
name = input('What is your name? ')

faveColor = input('Hi ' + name + ', what is your favorite color?')
print(name + ', I like ' + faveColor + ' too!')


birthYear = input('What year were you born in Mr. '+ name + '?')
age = 2019 - int(birthYear)
#print(age)
print(f'Wow you are so old, {name}, {age} years old!')


weightKG = input(f'{name}, how much do you weigh in kilograms?')
weightP = float(weightKG)*2.2
print(f'You weigh {weightP} in pounds!')


lName = input(f"What's your last name?")
fullName = name + lName
print(f'Your name is soooooo long, {len(fullName)} letters!')


fruitNumber = input(f"You need to eat healthy! Pick a number from 0 to 6.")
fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"Eat this fruit:")
print(fruitList[int(fruitNumber)])
