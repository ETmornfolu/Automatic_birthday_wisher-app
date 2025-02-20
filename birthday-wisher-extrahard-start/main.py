##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from smtplib import *
import os
import random
from dotenv import load_dotenv

load_dotenv()


MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
# 1. Update the birthdays.csv
data_file = pandas.read_csv("birthdays.csv")
now = dt.datetime.today()
present_day = (now.day, now.month)


birthday_dict = {
    (data_row.day, data_row.month): data_row
    for (index, data_row) in data_file.iterrows()
}


if present_day in birthday_dict:
    birthday_person = birthday_dict[present_day]
    celebrants_name = birthday_person["name"]
    txt_files = [
        file for file in os.listdir("./letter_templates") if file.endswith(".txt")
    ]
    random_file = random.choice(txt_files)
    with open(file=f"./letter_templates/{random_file}", mode="r") as new_file:
        generated_file = new_file.read()
        birth_day_letter = generated_file.replace("[NAME]", birthday_person["name"])
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday {celebrants_name}\n\n{birth_day_letter}",
        )

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
