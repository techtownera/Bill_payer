import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lenght = len(names)

payer = random.randint(0, lenght-1)

print(names[payer], "is going to buy the meal today!")






