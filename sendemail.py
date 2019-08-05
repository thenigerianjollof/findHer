import serial
import smtplib, ssl
print("Hi. Welcome to FindHer. To create an account, fill the next questions correctly")
user = input("What is your name?")
print("Hi ", user,", FindHer works by creating a handler account. A handler is an individual you trust with the knowledge of your position. You have to create a hodler accout by entering their email address. We do not share this information.")
holder= input("What is the email of your holder?")
port = 465  # For SSL
location = "Starbucks"
sender_email = "findHer012@gmail.com"
receiver_email = holder
message = ("""\
Subject: Holder alert.
Hi! this is the first email from findHer. you have just been listed as a holder. If you know who listed you, recognize this email as not a spam.""")
messageB = ("""
Subject: Location Alert.

She shared her location""")
        # Create a secure SSL context

print("Click the Button once to initiate your email and twice to share your location")
arduino = serial.Serial('COM3', 9600, timeout=.1)
while True:
    data = str(arduino.readline()[:-2]) #the last bit gets rid of the new-line chars
    if data == "b'send'":
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("findHer012@gmail.com", "atrevlli")
            server.sendmail(sender_email, receiver_email, message)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("findHer012@gmail.com", "atrevlli")
            server.sendmail(sender_email, receiver_email, messageB)
            break
    else:
        continue
