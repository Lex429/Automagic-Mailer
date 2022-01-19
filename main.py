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


EMAIL_ADDRESS  =  input("Email: ")
EMAIL_PASSWORD =  input("Password: ")
contacts = input('Contact? ')

tday = datetime.date.today()

Shift = input("Shift 1st or 2nd: ")




def staffmarkemail1st():
    s = "Staffmark Report " + Shift + " " + "Shift " + tday.strftime("%m-%d-%Y")



    one = input("Mcdonald, Ronald'")
    two = input("Berry, Allan")
    three = input("Grimes, Gordan")
    four = input("Johnson, flash")

    msg = EmailMessage()
    msg['Subject'] = (s)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(
        'Linda,  These are the people that reported to work on ' + tday.strftime("%m-%d-%Y ") + Shift + ' shift \n'
        '\n\n Mcdonald, Ronald' + one + '\n'
        'Berry, Allan' + two + '\n'
        'Grimes, Gordan' + three + '\n'
        'Johnson, flash' + four + '\n')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def staffmarkemail2nd():

    s = "Staffmark Report " + Shift + " " + "Shift " + tday.strftime("%m-%d-%Y")


    one = input("Jim Halpert")
    two = input("Dwight, Shrute")
    three = input("Evans, Montell")
    four = input("Riley, Mario")

    msg = EmailMessage()
    msg['Subject'] = (s)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(
        'Linda,  These are the people that reported to work on ' + tday.strftime("%m-%d-%Y ") + Shift + ' shift \n'
        '\n\n '
        'Jim Halpert' + one + '\n'
        'Dwight, Shrute' + two + '\n'
        'Evans, Montell' + three + '\n' 
        'Riley, Mario' + four + '\n')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if Shift == ('1st'):
    staffmarkemail1st()

if Shift == ('2nd'):
    staffmarkemail2nd()