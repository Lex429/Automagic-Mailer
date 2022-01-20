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
    # Any computation you do, if you can you should try to pull it up to a variable
    # it makes the value appear more standard and is better for performance.
    today_str = today.strftime("%m-%d-%Y")
    # f-strings allow you to inject variables in a cleaner way than adding, and
    # you don't run into as many issues like the compiler trying to do math with
    # strings depending on the order.
    subject = f"Staffmark Report {shift} shift for {today_str}"


    content_str = (
        f"Linda, these are the people that reported to work for shift {shift} on {today_str}\n"
        f"\n\n"
    )

    for employee in employees:
        content_str += f"{employee['name']} - {employee['email']}\n"

    msg = EmailMessage()
    msg['Subject'] = (subject)
    msg['To'] = recipient
    msg.set_content(content_str)

    # Personal preference, but I like to pull utilities like sending the email into their own
    # function. It makes it easier to track down problems and expand in the future
    send_email(msg)

def send_email(email_message):
    email_message['From'] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email_message)

# Function to fetch the employees given a specific shift
def fetch_employees(shift):
    if shift == 1:
        return [{
            'name': 'Mcdonald, Ronald',
            'email': 'ronald.mcdonald@gmail.com'
        }, {
            'name': 'Berry, Allan',
            'email': 'allan.berry@gmail.com'
        }, {
            'name': 'Grimes, Gordan',
            'email': 'gordan.grimes@gmail.com'
        }, {
            'name': 'Johnson, Flash',
            'email': 'flash.johnson@gmail.com'
        }]

    if shift == 2:
        return [{
            'name': 'Halpert, Jim',
            'email': 'jim.halpert@gmail.com'
        }, {
            'name': 'Schrute, Dwight',
            'email': 'dwight.schrute@gmail.com'
        }, {
            'name': 'Evans, Montell',
            'email': 'montell.evans@gmail.com'
        }, {
            'name': 'Riley, Mario',
            'email': 'mario.riley@gmail.com'
        }]


# This is basically like main() in other languages. Doing it like this will allow you to
# accept command line arguments
if __name__ == "__main__":
    shift = input("Shift to report: ")
    recipient = input("Email to send report: ")

    employees = fetch_employees(int(shift))
 
    staffmarkemail(shift, employees, recipient)
