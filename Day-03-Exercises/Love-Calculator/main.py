# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_string = name1 + name2
lower_case = combine_string.lower()

t = combine_string.count("t")
r = combine_string.count("r")
u = combine_string.count("u")
e = combine_string.count("e")

true = t + r + u + e

l = combine_string.count("l")
o = combine_string.count("o")
v = combine_string.count("v")
e = combine_string.count("e")

love = l + o + v + e

score = str(f"{true}{love}")

if score <= "10" and score >= "80":
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= "40" and score <= "50":
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

