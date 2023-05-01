# Imports.
import shodan as shodan
import os
import sys
import json
import requests
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
    key = data["shodan"]

# Program.
def run_shodan():
    # Get API and base.
    direct_url = ("https://www.shodan.io/")
    extend_url = ("host/")
    key_raw = ("/raw?key=")
    # Additional API information.
    SHODAN_API_KEY = (f"{key}")
    api = shodan.Shodan(SHODAN_API_KEY)
    host_ip = input(f"\n{print_question} IP: ")
    host = api.host(f'{host_ip}')
    # Print information from API.
    print(f"{print_prompt}","ISP: {}".format(host.get('isp', 'n/a'))) # Get ISP.
    print(f"{print_prompt}","Organization: {}".format(host.get('org', 'n/a'))) # Get Org
    print(f"{print_prompt}","Location: {}, {}".format(host.get('country_name', 'n/a'), host.get('city', 'n/a')))
    print(f"{print_prompt}","Long/Lat: {} | {}".format(host.get('longitude','n/a'), host.get('latitude','n/a'))) # Get Lat/Long.
    print("\nReserve API:")    
    # Reserve API and base.
    reserve_direct_url = ("http://ip-api.com/")
    reserve_extend_url = ("json/")
    r = requests.get(f'{reserve_direct_url}{reserve_extend_url}{host_ip}')
    r_dict = r.json()
    # Print information from API.
    print(f"{print_prompt}", "ISP:", r_dict['isp'])
    print(f"{print_prompt}","Location:", r_dict['city'], "|", r_dict['zip'])
    # Ports check.
    print("\nPorts:")
    for item in host['data']:
        print(f"{print_prompt}","{} | {}".format(item['port'], item['transport']))
        continue
    # Vuln check.
    print("\nVulns:")
    os.system(f"wget -q -O report.log {direct_url}{extend_url}{host_ip}{key_raw}{key}")
    with open('report.log') as file:
        contents = file.read()
        search_word = ("SAFE")
        if search_word in contents:
            print (f'{print_notice} Heartbleed: {Fore.GREEN}SECURE{print_text}\n')
        else:
            print (f'{print_notice} Heartbleed: {Fore.RED}UNSECURE / DATA NOT AVAILABLE{print_text}\n')
    os.system("rm report.log")
# Run Shodan module.
if __name__ == '__main__':
    run_shodan()