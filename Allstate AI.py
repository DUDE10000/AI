import pandas as pd
import webbrowser
import os
import ssl
from email.message import EmailMessage
import smtplib

name = input("Hello my name is Expo what is your name? ")
dayhow = input("How was your day? ")

if "good" in dayhow:
    print("Im happpy you had a",dayhow,"day")



elif "Good" in dayhow:
    print("Im happpy you had a",dayhow,"day")

elif "Ok" in dayhow:
   print("Im happpy you had a",dayhow,"day")

elif "ok" in dayhow:
    print("Im happpy you had a",dayhow,"day")

elif "nice" in dayhow:
    print("Im happpy you had a",dayhow,"day")

elif "Nice" in dayhow:
    print("Im happpy you had a",dayhow,"day")


else:
   print("Im sorry you had a",dayhow,"day")

whatneeded = input("What can i assist you with today: getting a qoute or contacting a agent? ")
#Qoute Needed
if "getting a qoute" in whatneeded:
    print("Okay I need a few things")
    dvl = input("What is your license number? ")
    phone = input("What is your phone number? ")
    email = input("What is your email? ")

elif "Getting a Qoute" in whatneeded:
    print("Okay I need a few things")
    dvl = input("What is your license number? ")
    phone = input("What is your phone number? ")
    email = input("What is your email? ")

elif "Qoute" in whatneeded:
    print("Okay I need a few things")
    dvl = input("What is your license number? ")
    phone = input("What is your phone number? ")
    email = input("What is your email? ")

elif "qoute" in whatneeded:
    print("Okay I need a few things")
    dvl = input("What is your license number? ")
    phone = input("What is your phone number? ")
    email = input("What is your email? ")
    corr = input("Is this information correct? ")
#Everything Correct
if "yes" in corr:
    print("Thank you for this information!")

elif "Yes" in corr:
    print("Thank you for this information!")

#Email
email_sender = 'allstateqoutebot@gmail.com'
email_password = 'ijxnhdqcwuowoyys'
email_reciever = 'anarchygaming1500@gmail.com'

subject =  name
body =("DVL:",dvl,"Phone:",phone,"Email",email,"Name",name)


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content("Name: " + name + "License Number: " + dvl + "Phone number: " + phone + "Email: " + email)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

#Incorrect things
if "No" in corr:
    incorr = input("Ok what informtion is incorrect? ")

if "no" in corr:
    incorr = input("Ok what informtion is incorrect? ")
#Correct License
if "license number" in incorr:
    dvl = input("What is the correct license number? ")
    corr = input("Is this correct license number? ")

elif "License Number" in incorr:
    dvl = input("What is the correct license number? ")
    corr = input("Is this correct license number? ")
#Correct Phone
elif "Phone" in incorr:
    phone = input("What is the correct phone number? ")
    corr = input("Is this correct phone number? ")

elif "phone" in incorr:
    phone = input("What is the correct phone number? ")
    corr = input("Is this correct number? ")
#Correct Email
elif "Email" in incorr:
    email = input("What is the correct email? ")
    corr = input("Is this correct email? ")

elif "email" in incorr:
    email = input("What is the correct email? ")
    corr = input("Is this correct email? ")
#Agent Contacting
if "contacting a agent" in whatneeded:
    print("To contact a agent please call (508) 638-6112")

if "Contacting a Agent" in whatneeded:
    print("To contact a agent please call (508) 638-6112")

if "contact agent" in whatneeded:
    print("To contact a agent please call (508) 638-6112")

if "Contact Agent" in whatneeded:
    print("To contact a agent please call (508) 638-6112")
#Email
email_sender = 'allstateqoutebot@gmail.com'
email_password = 'ijxnhdqcwuowoyys'
email_reciever = 'anarchygaming1500@gmail.com'

subject =  name
body ="DVL:",dvl,"Phone:",phone,"Email",email,"Name",name



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content("Name: " + name + "License Number: " + dvl + "Phone number: " + phone + "Email: " + email)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())