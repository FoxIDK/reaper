# Imports
import sys
import json
import os
import requests
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]")
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]")
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]")

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
                    name = data2[j]['commit']['author']['name']
                    email = data2[j]['commit']['author']['email']
                    if email in emails:
                        pass
                    else:
                        emails.append(email)
                        print(f"{print_prompt} • User: {name} \n{print_alert} • Email: {email}")
            except Exception:
                print("\nFailed to get further repo commits | Issue .")

# Error handling
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

if __name__ == '__main__':
    github()