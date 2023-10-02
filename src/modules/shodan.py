# Imports.
import shodan as shodan
import os
import sys
import json
import requests
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")

with open('var/api_config.json') as f:
    data = json.load(f)
    key = data["shodan"]

def run_shodan():
    # Prerequisites and inputs
    direct_url = ("https://www.shodan.io/")
    extend_url = ("host/")
    key_raw = ("/raw?key=")
    SHODAN_API_KEY = (f"{key}")
    api = shodan.Shodan(SHODAN_API_KEY)
    host_ip = input(f"\n{print_question} IP: ")
    host = api.host(f'{host_ip}')

    # Info from API
    print(f"{print_prompt}","ISP: {}".format(host.get('isp', 'n/a')))
    print(f"{print_prompt}","Organization: {}".format(host.get('org', 'n/a')))
    print(f"{print_prompt}","Location: {}, {}".format(host.get('country_name', 'n/a'), host.get('city', 'n/a')))
    print(f"{print_prompt}","Long/Lat: {} | {}".format(host.get('longitude','n/a'), host.get('latitude','n/a')))
    print("\nReserve API:")    
    # Info from reserve API
    reserve_direct_url = ("http://ip-api.com/")
    reserve_extend_url = ("json/")
    r = requests.get(f'{reserve_direct_url}{reserve_extend_url}{host_ip}')
    r_dict = r.json()
    print(f"{print_prompt}", "ISP:", r_dict['isp'])
    print(f"{print_prompt}","Location:", r_dict['city'], "|", r_dict['zip'])

    # Ports and vulns
    print("\nPorts:")
    for item in host['data']:
        print(f"{print_prompt}","{} | {}".format(item['port'], item['transport']))
        continue
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

if __name__ == '__main__':
    run_shodan()