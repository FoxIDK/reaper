# Imports
import os
import sys
import json
import requests
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")

with open('var/api_config.json') as f:
    data = json.load(f)
    key = data["number"]

def phone():
    # Prerequisites and inputs
    direct_url = ("https://api.numlookupapi.com/")
    extend_url = ("v1/validate/")
    key_raw = ("?apikey=")
    ndc = input(f"\n{print_question} National code (+44): ")
    number = input(f"{print_question} Number: ")
    r = requests.get(f'{direct_url}{extend_url}{ndc}{number}{key_raw}{key}')
    r_dict = r.json()

    # Info from API
    print(f"{print_prompt}","Live:", r_dict['valid'])
    print(f"{print_prompt}","Country:", r_dict['country_name'], "|", r_dict['country_code'])
    convert = lambda inp : inp if len(inp) > 0 else "n/a"
    print(f"{print_prompt}","Location:", convert(r_dict['location']))
    print(f"{print_prompt}","Carrier:", r_dict['carrier'])
    print(f"{print_prompt}","Line type:", r_dict['line_type'], "\n")

if __name__ == '__main__':
    phone()