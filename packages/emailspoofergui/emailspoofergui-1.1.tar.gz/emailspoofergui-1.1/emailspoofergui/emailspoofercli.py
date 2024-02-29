import subprocess
import getpass
import json
import os
import time
from colorama import Fore, Style

def print_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for speed
    print()
    
def print_colored_figlet_text(text, color):
    os.system(f"figlet -f slant '{text}' > temp_figlet.txt")  # Generate figlet text to a temporary file
    with open("temp_figlet.txt", "r") as file:
        figlet_output = file.read()
    os.remove("temp_figlet.txt")  # Remove temporary file

    colored_text = f"{color}{figlet_output}{Style.RESET_ALL}"  
    # Apply color after figlet
    print(colored_text) 



def send_email():
    print_colored_figlet_text("KORISHEE THE CYBERMASTER", Fore.GREEN)
    print_with_animation(f"{Fore.RED}PRESENTING A AUTOMATED REMOTE ACCESS TROJEN BINDERS FROM")
    # Read configuration from file
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("Config file not found or invalid.")
        return
    
    print_with_animation(f"{Fore.RED}Please enter the credentials to send spoofed mail")
    sender_name = input("Enter sender's name and email (e.g., 'From DBBL Support <ccs.cmc@dutchbanglabank.com>'): ")
    receiver_email = input("Enter recipient's email: ")
    subject = input("Enter the email subject: ")
    message = input("Enter the message: ")

    sendemail_command = f"sendemail -xu {config['username']} -xp {config['password']} -s {config['smtp_server']} -f {sender_name} -t {receiver_email} -u '{subject}' -m '{message}'"

    try:
        subprocess.run(sendemail_command, shell=True, check=True)
        print("Email sent successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Usage - Execute the function to send the email
send_email()
