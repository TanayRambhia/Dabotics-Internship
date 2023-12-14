import random
import smtplib
import getpass
import email.message
import re

def generate_otp():
    return str(random.randint(100000, 999999))  # Generate a 6-digit OTP

def send_email(receiver_email, otp):
    sender_email = "tanayrambhia204@gmail.com"  # Replace with your Gmail email address
    app_password = "dyyj bwos tbil khfn"  # Replace with the generated app password

    message = email.message.EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your OTP"

    message.set_content(f"Your OTP is: {otp}")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail's SMTP server and TLS port
        server.starttls()
        server.login(sender_email, app_password)  # Use the app password here
        server.send_message(message)
        server.quit()
        print("OTP sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def validate_email(email):
    # Simple email validation using regular expression
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def main():
    receiver_email = input("Enter your email address: ")
    while not validate_email(receiver_email):
        print("Invalid email address format. Please enter a valid email.")
        receiver_email = input("Enter your email address: ")

    otp = generate_otp()
    send_email(receiver_email, otp)

    entered_otp = input("Enter the OTP received in your email: ")

    if entered_otp == otp:
        print("OTP verified. Access granted.")
    else:
        print("Invalid OTP. Access denied.")

if __name__ == "__main__":
    main()
