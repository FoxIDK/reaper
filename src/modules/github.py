# Imports.
import sys # System stuff.
import json # Used for handling JSON data.
import os # Operating System functions.
import requests # Making requests.
from colorama import Fore # For text colour.

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Config (Prints).
print_text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
print_dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
print_disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Program.
def github():
    try:
        username = input(f"\n{print_question} GitHub username: ")
        print(f"\n{print_notice} Checking: {username} for repos.\n")
        r = requests.get(f'https://api.github.com/users/{username}/repos')

        data = json.loads( r.text )
        for i in range(len(data)):
            url = data[i]['html_url']
            print(f'{print_prompt} • {url}')

        emails = []
        print(f"\n{print_notice} Checking: {username} for details.\n")
        for i in range(len(data)):
            repo = data[i]['full_name']
            r2 = requests.get(f'https://api.github.com/repos/{repo}/commits')
            data2 = json.loads( r2.text )
            try:
                for j in range(len(data2)):
                    name = data2[j]['commit']['author']['name'] # Name data to data2.
                    email = data2[j]['commit']['author']['email'] # Email data to data2.
                    if email in emails:
                        pass
                    else:
                        emails.append(email)
                        print(f"{print_prompt} • User: {name} \n{print_alert} • Email: {email}")
            except Exception:
                print("Failed to get repo commits | potential rate limiting - try again later.")
# Error handling.
    except KeyboardInterrupt:
        print(f"\n{print_exited} {print_notice} {print_successfully}\n")
        print(f'{print_notice} You interrupted the program.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ValueError:
        print(f"\n{print_exited} {print_notice} {print_successfully}\n")
        print(f'{print_notice} You entered invalid data into a field.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# Run github module.
if __name__ == '__main__':
    github()