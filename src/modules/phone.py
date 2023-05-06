# Imports.
import os # Operating System functions.
import sys # System stuff.
import json # Used for handling JSON data.
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

# API.
with open('var/api_config.json') as f:
    data = json.load(f)
    key = data["number"]

# Program.
def phone():
    # Get API and base.
    direct_url = ("https://api.numlookupapi.com/")
    extend_url = ("v1/validate/")
    key_raw = ("?apikey=")
    ndc = input(f"\n{print_question} National code (+44): ")
    number = input(f"{print_question} Number: ")
    # Get information from API.
    r = requests.get(f'{direct_url}{extend_url}{ndc}{number}{key_raw}{key}')
    r_dict = r.json()
    # Print information from API.
    print(f"{print_prompt}","Live:", r_dict['valid'])
    print(f"{print_prompt}","Country:", r_dict['country_name'], "|", r_dict['country_code'])
    convert = lambda inp : inp if len(inp) > 0 else "n/a"
    print(f"{print_prompt}","Location:", convert(r_dict['location']))
    print(f"{print_prompt}","Carrier:", r_dict['carrier'])
    print(f"{print_prompt}","Line type:", r_dict['line_type'], "\n")

# Run phone module.
if __name__ == '__main__':
    phone()