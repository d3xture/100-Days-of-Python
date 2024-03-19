import smtplib
import pandas
import random
import datetime as dt

MY_EMAIL = "abc"
PASSWORD = "xyz"
dfs = []
birthday_wish = ""
file_paths = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Setting Up Now Time
now = dt.datetime.now()
month = now.month
today = now.day

# Reading CSV
df = pandas.read_csv("birthdays.csv")

# Appending all the wishes
for file in file_paths:
    with open(file) as f:
        template = f.read()
        dfs.append(template)

# Getting Hold From Csv File
for index, row in df.iterrows():
    name = row["name"]

    if month == row["month"] and today == row["day"]:

        # Getting Hold of random letter
        random_letter = random.choice(dfs)
        birthday_wish = random_letter.replace("[NAME]", name)

        # Sending Over the letter via email

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="d3xture@yahoo.com",
                                msg=f"Subject: Happy Birthday\n\n {birthday_wish}",
                                )

    else:
        print("No birthday today!")

