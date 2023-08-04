age = input("What is your current age? ")

age_as_int = int(age)
year_remaining = 90 - age_as_int
days_remaining = year_remaining * 365
weeks_reamining = year_remaining * 52
months_remainig = year_remaining * 12

message = (f"You have {days_remaining} days, {weeks_reamining} weeks, and {months_remainig} months left.")
print(message)

