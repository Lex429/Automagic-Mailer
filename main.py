#!usr/bin/python3

import smtplib
import datetime
from email.message import EmailMessage


# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# This is a prototype program for an auto emailer

# Thank-you for checking out and helping with this project!!! :)

# in order to test must input a valid gmail address and password
# You can delete the input's and place the info in the variables as strings to save your self from reinputting each time
# you will also need a valid gmail to recieve the incomming emails
# I reccomend using the same email used in EMAIL_ADDRESS for testing purposes


# EMAIL_ADDRESS  =  input("Email: ")
# EMAIL_PASSWORD =  input("Password: ")
# contacts = input('Contact? ')

# Move all this to one function with variables, it prevents duplication and makes
# expanding easier, for instance to add shift 3, 4, 5, and 6 you wouldn't have to 
# change anything.


def staffmarkemail(shift, employees, recipient):
    today = datetime.date.today()
    today_str = today.strftime("%m-%d-%Y")
    subject = f"Staffmark Report {shift} shift for {today_str}"
    content_str = (
        f"Linda, these are the people that reported to work for shift {shift} on {today_str}\n"
        f"\n\n"
                  )


    for names in []:
        content_str += f"{names['name']}\n"


    msg = EmailMessage()
    msg['Subject'] = (subject)
    msg['To'] = recipient
    msg.set_content(content_str)

    # i really like this didnt even think about that!!!!
    send_email(msg)



def send_email(email_message):

    EMAIL_ADDRESS = input('')
    EMAIL_PASSWORD = input('')
    email_message['From'] = EMAIL_ADDRESS
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email_message)



# Function to fetch the employees given a specific shift
# this is great! however i dont need their emails included.
# the body of the email should auto print their names and then send out an email body looking like this
# 'Mcdonald, Ronald - here
#  Berry, Allan -  (out sick) <- this part to be the user input
#  Grimes, Gordan - no show
#  Johnson, Flash - here

# so auto print the names and then accept user input for weather or not they showed up.

def fetch_employees(shift):
    if shift == 1:
        return
    names = {}
    filename = "names1.txt"
    with open(filename) as f:
        for line in f:
            (key, val) = line.strip().split('.')
            names[int(key)] = val

    if shift == 2:
        return
    names = {}
    filename = "names2.txt"
    with open(filename) as f:
        for line in f:
            (key, val) = line.strip().split('.')
            names[int(key)] = val



if __name__ == "__main__":
    shift = input("Shift to report: ")
    recipient = input("Email to send report: ")

    employees = fetch_employees(int(shift))

    staffmarkemail(shift, employees, recipient)

