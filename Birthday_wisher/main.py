import smtplib

#my_email = 'vecniche@gmail.com'
#password = 'bxiqoeypnwpfwluc'

#connection = smtplib.SMTP('smtp.gmail.com')
#connection.starttls()
#connection.login(user=my_email, password=password)
#connection.sendmail(from_addr=my_email, to_addrs="geniusniche@gmail.com", msg="Hellooo")

import datetime as dt
import random
#now = dt.datetime.now()

#print(now)


#MY_EMAIL = 'vecniche@gmail.com'
#MY_PASSWORD = 'Obinna1993'

#now = dt.datetime.now()
#weekday = now.weekday()
#if weekday == 5:
MY_EMAIL = 'email@gmail.com'
MY_PASSWORD = 'password'

##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random
# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
today_tuple = (datetime.now().month, datetime.now().day)

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as file:
        content = file.read()
        content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL, password= MY_PASSWORD,
        )
        connection.sendmail(
            from_addr= MY_EMAIL, to_addrs= birthday_person['email']
        )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




