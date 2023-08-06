# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_names = []
new_names.extend(names)

length = len(names)

random_generator = random.randint(0, length - 1)

print(f"{new_names[random_generator]} is going to buy the mean today!")
